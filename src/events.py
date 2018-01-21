from flask_restful import Resource
from opentok import MediaModes
from os import getenv
from src import api, ot
from src.store import listeners, venters
from time import sleep

SESH_IDX = 0
TOKEN_IDX = 1

def create_session_token(queue1, queue2):
    if queue2:
        sesh = queue2.pop(0)
    else:
        s = ot.create_session(media_mode=MediaModes.routed)
        sesh = {
            'id': s.session_id,
            'token': s.generate_token()
        }
        queue1.append(sesh)
    return sesh

@api.resource('/vent')
class Vent(Resource):
    def get(self):
        return create_session_token(venters, listeners)

@api.resource('/listen')
class Listen(Resource):
    def get(self):
        return create_session_token(listeners, venters)
