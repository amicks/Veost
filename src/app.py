from flask import abort, jsonify
from os import getenv
from src import api, app, db
from src.events import pair_from_queue, new_roaster, new_venter

def setup_app():
    db_uri = getenv('SQLALCHEMY_DATABASE_URI')
    if db_uri:
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    else:
        abort(401)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def setup_api(application):
    with application.app_context():
        api.init_app(application)

def setup_db(application, sqlalchemy_bind):
    with application.app_context():
        sqlalchemy_bind.init_app(application)
        sqlalchemy_bind.create_all()

@app.route('/')
def landing_page():
    return 'foo'

if __name__=='__main__':
    setup_app()
    setup_api(app)
    setup_db(app, db)
    app.run(debug=True)
