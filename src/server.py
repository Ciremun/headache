import os
from threading import Thread

from flask import Flask, Response
from gevent.pywsgi import WSGIServer

from .log import logger

app = Flask(__name__)

def run():
    wsgi = WSGIServer(('0.0.0.0', int(os.environ.get('PORT'))), app)
    logger.info('run server')
    wsgi.serve_forever()

@app.route('/')
def uwu():
    return Response(200)

serverThread = Thread(target=run)
serverThread.start()
