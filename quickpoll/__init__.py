#!/usr/bin/env python

import yaml

from quickpoll.poll import Poll


def get_polls():
    """Loads up the polls from the configuration file."""
    polls = []

    with open(Poll.config_file(), 'r') as stream:
        # Load the configuration from our YAML file.
        config = yaml.safe_load(stream)

        # Populate the polls.
        for p in config['polls']:
            polls.append(Poll.from_dict(p))

    return polls


# Minor test of the functionalities.
if __name__ == '__main__':
    get_polls()
