from turtle import *
from flask import Flask, flash, url_for, send_from_directory
from flask_socketio import SocketIO, emit

# from src.backend.init import init

app = Flask(__name__)
socket = SocketIO(app)

@app.route('/')
def home():
    return '''
    <!doctype html>
    <title>Grammar</title>
    <h1>choose grammar</h1>
    <script> 
    '''


if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', port=4000)
