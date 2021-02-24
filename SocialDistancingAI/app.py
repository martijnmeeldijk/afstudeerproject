from flask import Flask
from flask import render_template
from os import walk
import json
from flask import Response
import configparser



app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', page='dashboard')

@app.route('/counter')
def counter():
    return render_template('counter.html', page='counter')

@app.route('/settings')
def settings():
    return render_template('settings.html', page='settings')

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

@app.route("/get-config")
def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return Response(json.dumps(dict(config['USER'])),
                    status=200,
                    mimetype="application/json")

@app.route("/set-config/<key>/<value>")
def set_config(key, value):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['USER'][key] = value
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/set-default/<key>")
def set_default(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['USER'][key] = config['DEFAULT'][key]
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    