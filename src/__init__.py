from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
app = Flask(__name__)
