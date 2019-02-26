from turtle import *
from flask import Flask, flash, url_for, send_from_directory

# from src.backend.init import init

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <!doctype html>
    <title>Grammar</title>
    <h1>choose grammar</h1>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
