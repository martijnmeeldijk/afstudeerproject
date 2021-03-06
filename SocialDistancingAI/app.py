from flask import Flask
from flask import render_template
from flask import request
from os import walk
import json
from flask import Response
import configparser
from main import VideoOutput




app = Flask(__name__)
video_output = VideoOutput()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)

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

@app.route("/get-total-violations")
def get_total_violations():
    with open(f'logs/extra/total_violations', 'r') as f:
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

@app.route("/set-config/<key>/")
def set_config(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['USER'][key] = request.args.get('value').strip('"')
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


def gen(stream):
    while True:
        #get camera frame
        frame = stream.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video_output
    return Response(gen(video_output),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video')
def video():
    return render_template('video.html', page='video')

