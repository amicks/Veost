from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from opentok import OpenTok
from os import getenv

api = Api()
db = SQLAlchemy()
app = Flask(__name__)
ot = OpenTok(getenv('OT_API_KEY'), getenv('OT_API_SECRET'))
