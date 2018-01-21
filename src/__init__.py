from flask import Flask
from flask_restful import Api
from opentok import OpenTok
from os import getenv

api = Api()
app = Flask(__name__)
ot = OpenTok(getenv('OT_API_KEY'), getenv('OT_API_SECRET'))
