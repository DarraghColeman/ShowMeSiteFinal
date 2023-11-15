#!/usr/bin/env python

import yaml
from flask import Flask, abort, request

from quickpoll import Poll

# Define the global flask application object.
app = Flask(__name__)
poll_cache = None


def load_polls():
    """Loads up the polls from the configuration file."""
    global poll_cache
    polls = []

    with open(Poll.config_file(), 'r') as stream:
        # Load the configuration from our YAML file.
        config = yaml.safe_load(stream)

        # Populate the polls.
        for p in config['polls']:
            polls.append(Poll.from_dict(p))

    poll_cache = polls


def get_poll_from_name(name):
    """Gets a poll from our poll list by its name."""
    global poll_cache

    for poll in poll_cache:
        if poll.name == name:
            return poll

    return None


@app.route('/polls')
def list_polls():
    """Gets the list of the available polls."""
    global poll_cache
    json = {'polls': []}

    for poll in poll_cache:
        json['polls'].append(poll.__dict__)

    return json


@app.route('/poll/<name>')
def get_poll(name):
    """Gets a specific poll by its name."""
    poll = get_poll_from_name(name)
    if poll is not None:
        return poll.__dict__

    # No matching poll was found.
    abort(404)


@app.route('/vote/<name>', methods=['POST'])
def cast_vote(name):
    poll = get_poll_from_name(name)
    if poll is not None:
        poll.cast_vote(request.form.get('option'))
        return poll.__dict__

    # No matching poll was found.
    abort(404)


load_polls()
if __name__ == '__main__':
    app.run()
