#!/usr/bin/env python

import yaml
from flask import Flask, abort

from quickpoll import Poll


# Define the global flask application object.
app = Flask(__name__)

def load_polls():
    """Loads up the polls from the configuration file."""
    polls = []

    with open(Poll.config_file(), 'r') as stream:
        # Load the configuration from our YAML file.
        config = yaml.safe_load(stream)

        # Populate the polls.
        for p in config['polls']:
            polls.append(Poll.from_dict(p))

    app.config['POLLS'] = polls

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
    load_polls()
    app.run()
