
# Description

Render Jinja2 templates with a yaml-config

This scipt uses a customized yaml files to load variables to be used
during a Jinja2 template rendering


# Build

## Virtualenv

Install the wrapper for virtualenv

    sudo apt-get install virtualenvwrapper

or

    pip install virtualenvwrapper

if you used pip, make sure that the shell-functions had been sources

Create and activate a new virtualenv

    mkvirtualenv --python=/usr/bin/python3 render-jinja-with-yaml

Stop using the virtualenv

    deactivate

Activate an existing virtualenv

    workon render-jinja-with-yaml


## Link binaries to this repo

Do this if you want to develop the script or get update via `gi pull`:

    pip install -r requirements-devel.txt
    python setup.py develop

## Install the module

Use this if you want to have not connection between your virtualenv and
your git repository:

    pip install -r requirements.txt
    python setup.py install

## Create a whl file

This creates a share-able whl package

    python setup.py bdist_wheel

## Create a egg file

This creates a share-able egg package

    python setup.py bdist_egg

## Requirements

PIP requirements can be installed with `pip install -r <file>`

The `requirements-devel.txt` only contains direct dependencies without versions.
It should be used when developing colops.

The `requirements.txt` is a simple `pip freeze` dump of a know working state.

# Configure

Create the config-yml file containing all variables
which should be used in the template.

    ---
    mydict:
      key1: value1
    mylist:
    - item1
    - item2
    ...

Now reference the variables a template

    This is the value: {{ mydict['key1'] }}
    This are all list items:
    {% for item in mylist %}
        item: {{ item }}
    {% endfor %}

# Use

## Examples

    ~/snippets/render-jinja-with-yaml.py ~/vars/project1.yaml ~/templates/
