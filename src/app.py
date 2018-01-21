from flask import abort, jsonify, render_template, request
from os import getenv
from src import api, app
from src.events import new_roaster, new_venter

def setup_api(application):
    with application.app_context():
        api.init_app(application)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_session', methods=["POST"])
def new_session():
    if request.form.get('button') == 'vent':
        sesh = new_venter()
    elif request.form.get('button') == 'roast':
        sesh = new_roaster()

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    setup_api(app)
    app.run(debug=True)
