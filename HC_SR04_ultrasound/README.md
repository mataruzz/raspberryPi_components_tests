# HC-SR04 ultrasound
Testing its working principle and python library

## Configuration
Following GPION's name based on **pinout** command:
- Vcc to 5V
- Trig to GPIO18 (PWM)
- Echo to GPIO24 -> since GPIO support maximum voltage of 3.3V, 3 resistor had been used to reduce the voltage on GPIO24. It has been used a voltage partition (330+220 from gnd to gpio, 330 from gpio to echo)
- Gnd to GND

