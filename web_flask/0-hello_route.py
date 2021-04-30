#!/usr/bin/python3
'''Flask Module'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''First Flask Function'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
