from flask import Flask, send_from_directory
import random
import os

app = Flask(__name__)

@app.route('/api/randomprime')
def hello_world():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return str(random.choice(primes))

@app.route('/')
def serve_fe():
    return send_from_directory('FE', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('FE', path)

if __name__ == '__main__':
    app.run()
