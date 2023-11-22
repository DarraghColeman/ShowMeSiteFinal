# QuickPool

Super simple and easy to deploy web-based pooling software. This project allows
you to quickly spin up multiple pools, proving an easy to use API to intergrate
with any of your projects you might desire.

## Setting things up

In order to set this project up for testing all that you have to do is run this
command in order to install all of the project's dependencies:

```bash
pip3 install -r requirements.txt
```

After having the dependencies you'll need to create a new folder in the root
of the project called `config`, inside of that folder you have to create a file
called `polls.yml` which will contain the polls. If you need an example:

```yaml
---
polls:
  - name: 'simple-example'
    title: 'A simple example'
    desc: 'An example of a poll description and how to explain ambiguities to users.'
    options:
      - label: 'Option 1'
        value: 'op1'
      - label: 'Option 2'
        value: 'op2'
      - label: 'Option 3'
        value: 'op3'
      - label: 'Option 4'
        value: 'op4'
  - name: 'best-pet'
    title: 'What''s the best pet to have at home?'
    desc: 'Deciding what you next pet is going to be is an important thing, choose wisely!'
    options:
      - label: 'Cat'
        value: 'cat'
      - label: 'Dog'
        value: 'dog'
      - label: 'Bird'
        value: 'bird'
      - label: 'Snake'
        value: 'snake'
  - name: 'worst-pet'
    title: 'What''s the worst pet to have at home?'
    desc: 'Deciding what you next pet is going to be is an important thing, choose wisely!'
    options:
      - label: 'Bat'
        value: 'bat'
      - label: '<b>Squirrel</b>'
        value: 'squirrel'
      - label: 'Mosquitto'
        value: 'mosquitto'
      - label: 'Spider'
        value: 'spider'
      - label: 'Wasp'
        value: 'wasp'
```

After all this all that's needed in order to start the server up is to run:

```bash
python3 app.py
```

**Warning:** Every time you stop the server the votes are going to be lost.

## License

This software is licensed under the
[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) license.

