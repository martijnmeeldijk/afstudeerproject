from flask import Flask
from flask import render_template
from os import walk
import json
from flask import Response



app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', page='dashboard')

@app.route('/counter')
def counter():
    return render_template('counter.html', page='counter')

@app.route("/logs/<date>")
def get_log(date):
    with open(f'logs/{date}', 'r') as f:
        return f.read()

@app.route("/get-all-logs")
def get_all_logs():
    _, _, filenames = next(walk('logs'))
    return Response(json.dumps(filenames),
                    status=200,
                    mimetype="application/json")

@app.route("/get-violations")
def get_violations():
    with open(f'logs/extra/violations', 'r') as f:
        return f.read()

@app.route("/get-people")
def get_people():
    with open(f'logs/extra/people', 'r') as f:
        return f.read()