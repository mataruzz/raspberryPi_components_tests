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


# Setting CW direction
GPIO.output(cw_pin, GPIO.LOW)
GPIO.output(ccw_pin, GPIO.HIGH)
# Set initial DC to 0 -> stay still
pwm_wave.start(0)

def move_at_DC(dc):
    pwm_wave.ChangeDutyCycle(dc)  

duty_cycles = [i for i in range(10, 70, 1)] # big number of sample to have a smooth increase/decrease

while True:
    for dc in duty_cycles:
        pwm_wave.ChangeDutyCycle(dc)
        time.sleep(0.25) 
    
    duty_cycles.reverse()


# stop pwm
pwm_wave.stop()
time.sleep(1)

#release all GPIOs
GPIO.cleanup()