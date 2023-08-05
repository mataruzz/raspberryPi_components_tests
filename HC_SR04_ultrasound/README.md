# HC-SR04 Ultrasound Module Usage Guide
In this guide, you will find a comprehensive explanation and setup for utilizing a Raspberry Pi 3B+ (running Ubuntu Server 22.04) in conjunction with the HC-SR04 Ultrasound component.\
This project aims to help you grasp the fundamental principles of ultrasound technology and enhance your familiarity with the GPIO (General-Purpose Input/Output) library.

## Understanding the HC-SR04 Ultrasound Component
<p align="center">
  <img width = "250" src="https://github.com/mataruzz/arduino_components_tests/blob/main/HC_SR04_ultrasound/images/HC-SR04-Ultrasonic-Sensor.jpg">
</p>
An ultrasonic transmitter, which is essentially composed by a speacker, a receiver and a control circuit, send continuous high frequency ultrasonic waves. By measuring the time taken for these waves to travel back and forth, the distance can be calculated. It is mainly used for distance measurement and obstacle detection.\
The distance is determined using the formula:

***Distance*** ***=*** ***time*** * ***speed***

Here, the speed of sound in air is approximately 343 m/s.

## Configuration and Setup
**Note:** Raspberry Pi 3B+ GPIO pins support a maximum voltage of 3.3 V. Therefore, the use of a [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider) is necessary.

To view essential information about Raspberry Pi pins, including pin enumeration, use the following command:
```
pinout
```
Below is the configuration for connecting the HC-SR04 Ultrasound module in BOARD mode:
- Connect the Vcc channel to the 5V pin.
- Connect the Trig channel to GPIO18, which supports PWM (Pulse Width Modulation).
- Connect the Echo channel to GPIO24, ensuring its voltage is reduced to around 3V using a voltage divider.
- Connect the Gnd channel to a GND pin.

For the voltage division, two resistors are employed to achieve a voltage of approximately 3.125 V:
1. 550 Ω (combination of 330 Ω and 220 Ω resistors)
2. 330 Ω 

Refer to the following wiring diagram for a clearer visualization:
<p align="center">
  <img width = "700" src="https://github.com/mataruzz/arduino_components_tests/blob/main/HC_SR04_ultrasound/images/wiring_connection_HC_SR04.png">
</p>

## Running The Ultrasonic Test
To get started, follow these steps:

1. Clone the repository onto your Raspberry Pi 3B+ using the terminal:
```  
git clone https://github.com/mataruzz/arduino_components_tests.git
```
2. Navigate to the cloned directory:
```
cd arduino_components_tests
```
3. Execute the ultrasound test script:
```
./HC_SR04_ultrasound/ultrasound_test.py
```
By following these instructions, you'll successfully set up and run the HC-SR04 Ultrasound module with your Raspberry Pi 3B+. 
