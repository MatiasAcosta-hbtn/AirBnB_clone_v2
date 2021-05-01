#!/usr/bin/python3
'''Flask Module'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''First Flask Function'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    '''Second Flask Function'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    '''Third Flask Function'''
    return "C {}".format(str(text)).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    '''Forth Flask Function'''
    return "Python {}".format(str(text)).replace("_", " ")


if __name__ == "__main__":
    app.run()
