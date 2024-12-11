from application import app, db
from flask import jsonify

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def response(message: str, obj = None) -> dict[str, any]:
    if obj == None:
        json = {
            "error": False,
            "message": message
        }
    else:
        json = {
            "error": False,
            "message": message,
            "data": obj
        }

    return json

def response_image(message: str, link = None) -> dict[str, any]:
    if link == None:
        json = {
            "error": False,
            "message": message
        }
    else:
        json = {
            "error": False,
            "message": message,
            "url": link
        }

    return json

def err_response(e: str) -> dict[str, any]:
    json = {
        "error": True,
        "message": str(e)
    }

    return json

def get_all_talent():
    try:  
        cursor = db.talents.find({})
        documents = [document for document in cursor]
        
        if len(documents) == 0:
            return jsonify(err_response('Collection is empty!')), 404
        
        for document in documents:
            document['_id'] = str(document['_id']) 
        
        return jsonify(response('Data Retrieved Successfully.', documents)), 200
        
    except Exception as e:
        return jsonify(err_response(str(e))), 500
    
def get_all_images():
    try:  
        cursor = db.images.find({})
        documents = [document for document in cursor]
        
        if len(documents) == 0:
            return jsonify(err_response('Collection is empty!')), 404
        
        for document in documents:
            document['_id'] = str(document['_id']) 
        
        return jsonify(response('Data Retrieved Successfully.', documents)), 200
        
    except Exception as e:
        return jsonify(err_response(str(e))), 500

def create_talent(data):
    try:
        db.talents.insert_one(data)

        return jsonify(response('Data Created Successfully.')), 201

    except Exception as e:
        return jsonify(err_response(e)), 500
    
def get_talent_by_id(object_id):
    try:
        # Fetch the document by its id
        talent = db.talents.find_one({'_id': object_id})

        # If not found
        if talent is None:
            return jsonify(err_response('Data not found.')), 404
        
        talent['_id'] = str(talent['_id'])

        return jsonify(response('Data Found.', talent)), 200

    except Exception as e:
        return jsonify(err_response(str(e))), 404

def update_talent_by_id(object_id, data):
    try:
        result = db.talents.update_one({'_id': object_id}, {'$set': data})

        if result.matched_count == 0:
            return jsonify(err_response('Data not found for update.')), 404

        return jsonify(response('Data Updated Successfully.')), 200

    except Exception as e:
        return jsonify(err_response(str(e))), 500

def delete_talent_by_id(object_id):
    try:
        result = db.talents.delete_one({'_id': object_id})

        if result.deleted_count == 0:
            return jsonify(err_response('Data not found for deletion.')), 404

        return jsonify(response('Data Deleted Successfully.')), 200

    except Exception as e:
        return jsonify(err_response(str(e))), 500
    
def get_image_by_id(object_id):
    try:
        # Fetch the document by its id
        talent = db.images.find_one({'_id': object_id})

        # If not found
        if talent is None:
            return jsonify(err_response('Data not found.')), 404
        
        talent['_id'] = str(talent['_id'])

        return jsonify(response('Data Found.', talent)), 200

    except Exception as e:
        return jsonify(err_response(str(e))), 404
    
def delete_image_by_id(object_id):
    try:
        result = db.images.delete_one({'_id': object_id})

        if result.deleted_count == 0:
            return jsonify(err_response('Data not found for deletion.')), 404

        return jsonify(response('Data Deleted Successfully.')), 200

    except Exception as e:
        return jsonify(err_response(str(e))), 500