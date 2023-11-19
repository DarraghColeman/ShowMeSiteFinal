#!/usr/bin/env python

from os.path import abspath, dirname

from quickpoll.renderable import Renderable


class Poll(Renderable):
    """Abstraction of a poll defined in the configuration."""

    def __init__(self, name, title, desc='', options=None):
        if options is None:
            options = []

        self.name = name
        self.title = title
        self.desc = desc
        self.options = options

    @property
    def __dict__(self):
        # Build up the base structure.
        d = {
            'name': self.name,
            'title': self.title,
            'desc': self.desc,
            'votes': 0,
            'options': []
        }

        # Populate the options.
        for opt in self.options:
            d['options'].append(opt.__dict__)
            d['votes'] += opt.votes

        return d

    def cast_vote(self, value):
        """Casts a vote on an option by its value."""
        for opt in self.options:
            if opt.value == value:
                opt.cast_vote()

    @staticmethod
    def from_dict(d):
        """Builds up a Poll object from a dict (usually comes from the
        configuration)."""
        # Create the base poll object.
        self = Poll(d['name'], d['title'], d['desc'])

        # Populate the options.
        for opt in d['options']:
            self.options.append(Option.from_dict(opt))

        return self

    @staticmethod
    def config_file():
        """Location of the polls YAML configuration file."""
        return dirname(dirname(abspath(__file__))) + '/config/polls.yml'


class Option(Renderable):
    """A representation of a poll option."""

    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.votes = 0

    @property
    def __dict__(self):
        return {
            'label': self.label,
            'value': self.value,
            'votes': self.votes
        }

    def cast_vote(self):
        """Casts a vote on this option."""
        self.votes += 1

    @staticmethod
    def from_dict(d):
        """Builds up an option object from a dict (usually from the
        configuration)."""
        return Option(d['label'], d['value'])
