from flask import Flask
from flask import render_template
from os import walk
import json



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/logs/<date>")
def get_log(date):
    with open(f'logs/{date}.json', 'r') as f:
        return f.read()

@app.route("/get-all-logs")
def get_all_logs():
    _, _, filenames = next(walk('logs'))
    return json.dumps(filenames)

