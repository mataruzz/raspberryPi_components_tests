# Micro Servo SG90 Usage Guide
In this guide, you will find a comprehensive explanation and setup for utilizing a Raspberry Pi 3B+ (running Ubuntu Server 22.04) in conjunction with the Micro Servo SG90 component.\
This project aims to help you grasp the fundamental principles of micro servo technology and enhance your familiarity with the GPIO (General-Purpose Input/Output) library.

## Understanding the Micro Servo SG90 Component
<p align="center">
  <img width = "250" src="https://github.com/mataruzz/arduino_components_tests/blob/main/S90_servo_motor/images/micro-servo-motor-sg90.jpg">
</p>
The micro servo SG90 (datasheet <a href="http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf">here</a>) is a compact electromechanical device featuring internal gears and a control circuit. It operates based on PWM (Pulse Width Modulation) signals, which dictate its angular position within a specific range. This precise servo mechanism finds utility in robotics, radio control mechanisms, and automation systems, offering accurate and controlled rotational movement for various applications.

To achieve a specific angle with the micro servo SG90, the duty cycle of the PWM signal should be adjusted. A duty cycle of around 5% corresponds to a 0-degree angle, while a duty cycle of about 10% typically results in a 90-degree angle. Varying the duty cycle between these values allows precise control of the servo's rotational position.

## Configuration and Setup
To view essential information about Raspberry Pi pins, including pin enumeration, use the following command:
```
pinout
```
Below is the configuration for connecting the Micro Servo SG90 module in BOARD mode:
- Connect the Vcc channel (red wire) to the 5V pin.
- Connect the PWM channel (orange wire) to GPIO18, which supports PWM (Pulse Width Modulation).
- Connect the Gnd channel (brown wire) to a GND pin.

Refer to the following wiring diagram for a clearer visualization:
<p align="center">
  <img width = "700" src="https://github.com/mataruzz/arduino_components_tests/blob/main/S90_servo_motor/images/wiring_connection_S90_servo.png">
</p>

## Running The Micro Servo Test
To get started, follow these steps:

1. Clone the repository onto your Raspberry Pi 3B+ using the terminal:
```  
git clone https://github.com/mataruzz/raspberryPi_components_tests.git
```
2. Navigate to the cloned directory:
```
cd raspberryPi_components_tests
```
3. Execute the servo test script:
```
./S90_servo_motor/servo_test_PWM.py
```
By following these instructions, you'll successfully set up and run the Micro Servo SG90 module with your Raspberry Pi 3B+. 

### ***Update***:
Other tests have been developed (both in python and in Cpp) in order to manually recreate the PWM, setting 'HIGH' or 'LOW' the pin. To run these tests, the pin connected to the board must be a **NON** PWM_PIN.

4. Compile the C++ script:
```
g++ -o S90_servo_motor/servo_test S90_servo_motor/servo_test.cpp -lwiringPi
```
5. Execute the executable servo test
```
./S90_servo_motor/servo_test
```
