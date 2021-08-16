# handle the realtime functionality here, TODO import in app.py

# set dispatcher
import socketio
from src.handlers.Dispatcher import Dispatcher
from src.helpers.Logger import Logger

from flask_socketio import send, emit

try:
    from __main__ import socketio
except ImportError:
    from app import socketio

dispatcher = Dispatcher()

# set up microphone cache queue

# set up and connect socket

# trigger appropriate events on every definite result
    # might not work if the translate event takes too long

@socketio.on('connect')
def test_connect(auth):
    Logger.log_info("Socket connected - Audio Stream started")
    emit('connect response', {'message': 'Connected!'})

@socketio.on('disconnect')
def test_connect():
    Logger.log_info("Socket Disconnected - Audio Stream stopped")

@socketio.on('stream')
def handle_message(data):
    Logger.log_info('Received blob {} of size{}'.format(data['order'], data['size']))
    
Logger.log_info("Socket Handlers initialized")