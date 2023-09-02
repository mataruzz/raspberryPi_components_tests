#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
servoPin1 = 5

GPIO.setmode(GPIO.BCM) # check on "pinout"

GPIO.setwarnings(False)

def init():
  GPIO.setup(servoPin1, GPIO.OUT)
  
def servoPulse(servoPin, myangle):
  pulsewidth = (myangle*13) + 300 # The pulse width in microseconds
  GPIO.output(servoPin,GPIO.HIGH)
  time.sleep(pulsewidth/1000000.0)
  GPIO.output(servoPin,GPIO.LOW)
  time.sleep(20.0/1000 - pulsewidth/1000000.0) # The cycle of 20 ms
  # time.sleep(0.02)
  
try:
  init()
  while True:
    
    for i in range(0, 180):
      i = 180 - i
      servoPulse(servoPin1, i)
      
    for i in range(180, -1, -1):
      i = 180 - i
      servoPulse(servoPin1, i)
      
except KeyboardInterrupt:
  pass