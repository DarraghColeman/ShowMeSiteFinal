#!/usr/bin/env python3

import json
from abc import ABC


class Renderable(ABC):
    """Abstracts an object that can be rendered by the server."""

    def to_json(self):
        """JSON representation of the object."""
        return json.dumps(self.__dict__)
