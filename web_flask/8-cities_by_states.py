#!/usr/local/bin/python3
'''Flask Module'''


from flask import Flask, abort, render_template
from models import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities():
    """Display a HTML all Cities by states"""
    states_list = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(self):
    """Function that call close method"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
