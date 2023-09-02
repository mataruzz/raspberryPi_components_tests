#include </home/mataruzz/projects/raspberryPi_components_tests/S90_servo_motor/WiringPi/wiringPi/wiringPi.h>
#include <unistd.h>
#include <cstdio>
#include <string>
#include <string.h>

#define GPIO_PIN 5 // Use GPIO 21 (WiringPi numbering)

void servoPulse(const double& pwmOn, const double& delayOn){
    // Set the pin high for pwmOn 
    digitalWrite(GPIO_PIN, HIGH);
    usleep(pwmOn);

    // Set the pin low for the remaining cycle
    digitalWrite(GPIO_PIN, LOW);
    usleep(delayOn);
}


int main() {
    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

    // Set the pin as an output
    pinMode(GPIO_PIN, OUTPUT);

    // Variable definition
    double pwmOn; 
    std::string speed="m";
    double delayOn;    
    // min delay=2'000 -> Taking this time as the minimum [ms] before turning High the pin again
    // max delay=20'000

    while (1) {
        // Selecting desired speed
        if(speed == "f"){
            delayOn = 2'000;
        }else if(speed == "m"){
            delayOn = 11'000;
        }else if(speed == "s"){
            delayOn = 20'000;
        }else{
            printf("Error in selection of the speed\n");
            return -1;
        }

        for(int angle=0; angle<= 180; angle++)
        {
            pwmOn = angle*13 + 300; // In microseconds [us]
            servoPulse(pwmOn, delayOn);
        }
                
        for(int angle=180; angle>=0; angle--)
        {
            pwmOn = angle*13 + 300; // In microseconds [us]
            servoPulse(pwmOn, delayOn);

            // To make smoothier the stop before going back
            if (angle==1){ usleep(100000); }
        }

    }

    return 0;
}
