#!/usr/bin/python
from twilio.rest import Client
import RPi.GPIO as GPIO
import time

audio = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(audio, GPIO.IN)

account_sid = '$SID'
auth_token = '$AUTH'
client = Client(account_sid, auth_token)

def Msg(channel): 
   print("Detected, sending notification.")
   message = client.messages \
    .create(
         body='Hi, your nearby sound levels have crossed the limit set by you.',
         from_='+19124612542',
         to='+917827794110'
     )

   print(message.sid)

def callback(audio):
    if GPIO.input(audio):
      print("High")
      time.sleep(5)
      
GPIO.add_event_detect(audio, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(audio, callback)
GPIO.add_event_callback(audio, Msg)

while True:
  time.sleep(1)
