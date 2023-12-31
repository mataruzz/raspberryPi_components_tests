#!/usr/bin/python3
 
import RPi.GPIO as GPIO 
from time import sleep 

# Declaring how we want to declare our pin
GPIO.setmode(GPIO.BOARD)  #GPIO.BOARD consider the phisical number of pin
# GPIO.setmode(GPIO.BCM) #segue la numerazione del processore (si vede tramite pinout)
servoPin = 12 #29 #5 #12

# Declaration the pin's port and type
GPIO.setup(servoPin,GPIO.OUT) 

def rotate(pwm, deg):
  # formula to convert angle to duty cycle: (deg/18)+2
  return pwm.ChangeDutyCycle((deg/18)+2)

def main():
  # Declaring the actual used PWM pin and it's frequency. S90 use 50Hz (20ms as period)
  pwm=GPIO.PWM(servoPin,50)
  # Starting the servo at 0 degree
  pwm.start(2)  
  sleep(0.5)
  
  while True:
    # Operational mode selection
    op = input("Operationa mode?(c:continuous/s:single/e:end): ")
    
    rotations = [0, 45, 90, 135, 180]
    
    if op.upper() == "C":
      des_cycle = int(input("\t-How many half cycle: "))
      
      i, cycle = 0, 0
      flag = True
      while flag:      
        rotate(pwm, rotations[i])
        print(f"Rotating at angle: {rotations[i]}")
        #Waiting to complete the movement
        sleep(0.5)
        
        if i==4:
          i=0
          cycle += 1
          print(f"----- END OF CYCLE {cycle} -----")
          rotations.reverse()
          if cycle%des_cycle == 0:
            flag=False
        i+=1
        
    elif op.upper() == "S":
      angle = float(input("\t-Insert the desired degree angle: "))
      rotate(pwm, angle)
    elif op.upper() == "E":
      pwm.stop()  
      GPIO.cleanup() 
      return 0

  

if __name__ == '__main__':
  main()

