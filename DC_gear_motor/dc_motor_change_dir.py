#!/usr/bin/python3

#Libraries
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins definition
cw_pin = 20
ccw_pin = 21
pwm_pin = 0

# Set the motor driver's pin as OUTPUT
GPIO.setup(cw_pin , GPIO.OUT)
GPIO.setup(ccw_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

# Using pwm frequency of 100 Hz
f = 100
pwm_wave = GPIO.PWM(pwm_pin, f)

# Set initial DC to 0 -> stay still
pwm_wave.start(0)

def move_forward():
    #shutting down the power
    pwm_wave.ChangeDutyCycle(0)  
    time.sleep(0.35)
    GPIO.output(cw_pin, GPIO.LOW)
    GPIO.output(ccw_pin, GPIO.HIGH)
    # give time to reduce the speed almost to 0
    # Invert the rotation
    pwm_wave.ChangeDutyCycle(35)  
    
def move_backward():
    #shutting down the power
    pwm_wave.ChangeDutyCycle(0)    
    time.sleep(0.35)
    GPIO.output(cw_pin, GPIO.HIGH)
    GPIO.output(ccw_pin, GPIO.LOW)
    # give time to reduce the speed almost to 0

    # Invert the rotation
    pwm_wave.ChangeDutyCycle(35)  

cw_flag = 1
while True:
    if cw_flag:
        move_forward()
    else:
        move_backward()
        
    pwm_wave.ChangeDutyCycle(35)
    time.sleep(5)
    cw_flag = not cw_flag

# stop pwm
pwm_wave.stop()
time.sleep(1)

#release all GPIOs
GPIO.cleanup()