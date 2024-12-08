from dotenv import load_dotenv
from os import getenv
from flask import Flask
from flask_pymongo import PyMongo

load_dotenv('.env')

PASSWORD = getenv("password")
IMAGEBB_KEY = getenv("IMAGEBB_KEY")

app = Flask(__name__)
app.config['MONGO_URI'] = f"mongodb+srv://iniUser:{PASSWORD}@cluster0.0rsk1.mongodb.net/db_ventix?retryWrites=true&w=majority"
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

mongo = PyMongo(app)
db = mongo.db

from application import routes