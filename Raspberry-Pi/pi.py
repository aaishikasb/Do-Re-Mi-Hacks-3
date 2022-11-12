#!/usr/bin/python
import RPi.GPIO as GPIO
import time

audio = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(audio, GPIO.IN)

def callback(audio):
    if GPIO.input(audio):
      print "High"
    else:
      print "High"
      
GPIO.add_event_detect(audio, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(audio, callback)

while True:
  time.sleep(1)
