from flask import render_template, request, redirect, url_for
from os import getenv
from src import app
from src.events import new_roaster, new_venter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_session', methods=['POST'])
def new_session():
    if request.form.get('button') == 'vent':
        sesh = new_venter()
    elif request.form.get('button') == 'roast':
        sesh = new_roaster()
    return render_template('vent.html', session_id=sesh['id'], token=sesh['token'], api_key=getenv('OT_API_KEY'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
