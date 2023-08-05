# HC-SR04 ultrasound
![Alt text](https://github.com/mataruzz/arduino_components_tests/blob/main/HC_SR04_ultrasound/images/HC-SR04-Ultrasonic-Sensor.jpg)

An ultrasonic transmitter, which is essentially composed by a speacker, a receiver and a control circuit, send continuous high frequency ultrasonic waves. The distance, then, is computed by acquiring the time spent to travel back and forth, and multiplying this time by the sound speend (in air: 343 [m/s]).

***Distance*** ***=*** ***time*** * ***speed***

## Configuration
**REMEMBER:** raspberry's pi 3B+ GPIOs support **3.3** **V** as maximum voltage. For this reason, a [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider) is necessary.

- To see basic Raspberry pi information, including pin's enumeration:
```
pinout
```
Following BOARD mode to describe GPIO connections: 
- Vcc channel to 5V
- Trig channel to GPIO18, which is a PWM
- Echo channel to GPIO24 (partitioning its voltage around 3V)
- Gnd channel to GND

The voltage partition, to have a voltage of around *3.125* *V*, has been built using the following resistors:
1. 550 Ω -> (330 + 220) Ω
2. 330 Ω 

The connection scheme is depicted below:

![Alt text](https://github.com/mataruzz/arduino_components_tests/blob/main/HC_SR04_ultrasound/images/wiring_connection_HC_SR04.png)

## Running
Clone the repository on the raspberry pi 3B+:
```  
git clone https://github.com/mataruzz/arduino_components_tests.git
```
Run the script:
```
./HC_SR04_ultrasound/ultrasound_test.py
```

