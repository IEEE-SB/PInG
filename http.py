#!/usr/bin/env python
import gpio
from bottle import *

@route('/out/<pin>/<value>')
def show(pin,value):
	pin = gpio.Gpio(pin)
	pin.direction("out")
	pin.value(value)
	pin.unexport()


run(host='localhost', port=8080)
