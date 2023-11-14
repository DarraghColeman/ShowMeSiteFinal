#!/usr/bin/env python

from os.path import abspath, dirname

from quickpoll.renderable import Renderable


class Poll(Renderable):
    """Abstraction of a poll defined in the configuration."""

    def __init__(self, name, title, options=None):
        if options is None:
            options = []

        self.name = name
        self.title = title
        self.options = options

    @property
    def __dict__(self):
        # Build up the base structure.
        d = {
            'name': self.name,
            'title': self.title,
            'options': []
        }

        # Populate the options.
        for opt in self.options:
            d['options'].append(opt.__dict__)

        return d

    @staticmethod
    def from_dict(d):
        """Builds up a Poll object from a dict (usually comes from the
        configuration)."""
        # Create the base poll object.
        self = Poll(d['name'], d['title'])

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

    @property
    def __dict__(self):
        return {
            'label': self.label,
            'value': self.value
        }

    @staticmethod
    def from_dict(d):
        """Builds up an option object from a dict (usually from the
        configuration)."""
        return Option(d['label'], d['value'])
