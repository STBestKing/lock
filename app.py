# -*- coding: utf-8 -*-

import click
import RPi.GPIO as GPIO
import time
from flask import Flask, url_for




app = Flask(__name__)

state = GPIO.LOW
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)

# the minimal Flask application
@app.route('/')
def index():
    global state
    if state == GPIO.LOW:
        GPIO.output(12, GPIO.HIGH)
        state = GPIO.HIGH
        time.sleep(0.01)
        GPIO.output(12, GPIO.LOW)
        state = GPIO.LOW
        return '<h1>OPEN SUCCESSFUL</h1>'
    else:
        GPIO.output(12, GPIO.LOW)
        state = GPIO.LOW
        return '<h1>CLOSING</h1>'


# bind multiple URL for one view function
@app.route('/al')
def always():
    global state
    if state == GPIO.LOW:
        GPIO.output(12, GPIO.HIGH)
        state = GPIO.HIGH
        return '<h1>Always Open</h1>'
    else:
        GPIO.output(12, GPIO.LOW)
        state = GPIO.LOW
        return '<h1>CLOSING</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
