import os
from threading import Thread

from flask import Flask, Response, send_from_directory, render_template
from gevent.pywsgi import WSGIServer

from .log import logger

app = Flask(__name__, static_folder='../flask', template_folder='../flask/templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def run():
    wsgi = WSGIServer(('0.0.0.0', int(os.environ.get('PORT'))), app)
    logger.info('run server')
    wsgi.serve_forever()

@app.route('/')
def uwu():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

serverThread = Thread(target=run, daemon=True)
serverThread.start()
