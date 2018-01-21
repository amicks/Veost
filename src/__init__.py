from flask import Flask
from opentok import OpenTok
from os import getenv

app = Flask(__name__)
ot = OpenTok(getenv('OT_API_KEY'), getenv('OT_API_SECRET'))
