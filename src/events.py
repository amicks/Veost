from opentok import MediaModes
from src import ot
from src.store import roasters, venters

def pair_users(queue):
    if queue:
        sesh = queue.pop(0)
    else:
        s = ot.create_session(media_mode=MediaModes.routed)
        sesh = {
            'id': s.session_id,
            'token': s.generate_token()
        }
        queue.append(sesh)
    return sesh

def new_venter():
    return pair_users(venters)

def new_roaster():
    return pair_users(roasters)
