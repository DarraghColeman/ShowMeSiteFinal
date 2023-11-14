#!/usr/bin/env python

from flask import Flask, abort

import quickpoll

# Define the global flask application object.
app = Flask(__name__)
app.config['POLLS'] = quickpoll.get_polls()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/polls')
def list_polls():
    """Gets the list of the available polls."""
    json = {'polls': []}

    for poll in app.config['POLLS']:
        json['polls'].append(poll.__dict__)

    return json


@app.route('/poll/<name>')
def get_poll(name):
    """Gets a specific poll by its name."""
    for poll in app.config['POLLS']:
        if poll.name == name:
            return poll.__dict__

    # No matching poll was found.
    abort(404)


if __name__ == '__main__':
    app.run()
