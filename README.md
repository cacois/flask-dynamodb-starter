# Flask-DynamoDB-Starter

This is a starting point for Flask applications using AWS DynamoDB. It comes with Flask, Bootstrap 3, Flask-DebugToolbar, and working user registration and authentication with a very basic User model.

## Setup

Setup is pretty easy.

### Install Dependencies

    $ pip install -r requirements.txt

### Create DynamoDB local container

If you don't already have it installed, (https://docs.docker.com/engine/installation/)[install docker]

Then, run a DynamoDB container:

    $ docker run -d --name dynamodb -p 8000:8000 instructure/dynamodb

### Start the app

    $ python manage.py runserver

## Testing
