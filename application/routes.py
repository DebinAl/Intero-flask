import os
import requests
from bson import ObjectId
from flask import request, jsonify
from werkzeug.utils import secure_filename
from application import app, db, helper, IMAGEBB_KEY

import json
    
@app.route('/api/v1/cms/talents', methods=["GET", "POST"])
def talents():
    if request.method == "GET":
        return helper.get_all_talent()
        
    elif request.method == "POST":
        # get data from request body
        data =  request.get_json()
        return helper.create_talent(data)

@app.route('/api/v1/cms/talents/<string:_id>', methods=['GET', 'PUT', 'DELETE'])
def talent_id(_id):
    # Check if it's a valid ObjectId
    if not ObjectId.is_valid(_id):
        return jsonify(helper.err_response('Invalid ID format.')), 400

    object_id = ObjectId(_id)

    if request.method == 'GET':
        return helper.get_talent_by_id(object_id)

    elif request.method == 'PUT':
        # Get updated data from the request body
        data = request.get_json()
        return helper.update_talent_by_id(object_id, data)

    elif request.method == 'DELETE':
        return helper.delete_talent_by_id(object_id, db.talents)
    
@app.route('/api/v1/cms/images', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'GET':
        return helper.get_all_images()
    
    if request.method == "POST":
        if 'image' not in request.files:
            return jsonify(helper.err_response('No file part in the request.')), 400

        file = request.files['image']

        # If no file is selected
        if file.filename == '':
            return jsonify(helper.err_response('No file selected for uploading.')), 400

        # Check if the file is allowed
        if file and helper.allowed_file(file.filename):
            try:
                # Sanitize and secure the filename
                filename = secure_filename(file.filename)
                
                #upload to imagebb and retrieve the link
                with file.stream as image_stream:  # Ensure the file stream is passed
                    response = requests.post(
                        "https://api.imgbb.com/1/upload",
                        params={
                            'key': IMAGEBB_KEY,
                            'name': os.path.splitext(filename)[0],
                            'expiration': 1728000 # 20 days
                                },
                        files={'image': image_stream}
                    )

                if response.status_code == 200:
                    img_data = response.json()
                    print(json.dumps(img_data, indent=4))
                    link = img_data['data']['url']  # Retrieve the image URL from ImgBB
                    link =  link.replace('i.ibb.co', 'i.ibb.com')

                    # store image metadata in the database
                    image_data = {
                        "filename": filename,
                        "link": link
                    }
                    db.images.insert_one(image_data)

                return jsonify(helper.response_image('Image uploaded successfully.', link)), 201

            except Exception as e:
                return jsonify(helper.err_response(str(e))), 500

        else:
            return jsonify(helper.err_response('File type not allowed.')), 400
        
@app.route('/api/v1/cms/images/<string:_id>', methods=['GET', 'DELETE'])
def image_id(_id):
    # Check if it's a valid ObjectId
    if not ObjectId.is_valid(_id):
        return jsonify(helper.err_response('Invalid ID format.')), 400

    object_id = ObjectId(_id)

    if request.method == 'GET':
        return helper.get_image_by_id(object_id)

    elif request.method == 'DELETE':
        response = helper.delete_image_by_id(object_id)
        # if response[1] == 200:

        return response