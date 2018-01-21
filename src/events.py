from opentok import MediaModes
from os import getenv
from src import ot
from src.store import roasters, venters

def pair_from_queue(q):
    if q:
        sesh = q.pop(0)
    else:
        s = ot.create_session(media_mode=MediaModes.routed)
        sesh = {
            'id': s.session_id,
            'token': s.generate_token()
        }
        q.append(sesh)
    return sesh

def new_venter():
    return pair_from_queue(venters)

def new_roaster():
    return pair_from_queue(roasters)
