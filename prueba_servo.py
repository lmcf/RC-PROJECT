#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
  
#Setup servoPin as PWM output of frequancy 100Hz
servoPin=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(0)

pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)


pwm.stop()
GPIO.cleanup()

