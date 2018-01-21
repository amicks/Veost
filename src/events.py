from opentok import MediaModes
from os import getenv
from src import ot
from src.store import listeners, venters

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

def new_venter():
    return create_session_token(venters, listeners)

def new_listener():
    return create_session_token(listeners, venters)
