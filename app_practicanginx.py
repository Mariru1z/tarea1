from flask import Flask
import socket
import requests
import json

app = Flask(__name__)

counter = 0

@app.route('/')
def index():
    return 'Practica1 - creacion de una APIUrequest!'

@app.route('/count')
def count():
    container_id = socket.gethostname()
    global counter
    counter += 1
    return f'<body> <h1>You clicked this page {counter} times on server: {container_id}<h1> <body>'

@app.route('/holamundo/')
def holamundo():
    return 'HOLA MUNDO'

@app.route('/pruebadocker/')
def holadocker():
    return 'HOLA DOCKER'

@app.route('/nginx/')
def nginx():
    return '<body bgcolor=ff0000> <h1>ENDPOINT ACTIVADO NGINx!<H1> <body>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

