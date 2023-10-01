#include <wiringPi.h>
#include <unistd.h>
#include <vector>
#include <iostream>
#include <signal.h>

// Basic variable definition
int const cwPin = 20;
int const ccwPin = 21;
int const pwmPin = 0;
float const freq = 100.0; // Hz -> 1/f = 0.01 s

// Define the function to be called when ctrl-c (SIGINT) is sent to process
void signal_callback_handler(int signum) {
    std::cout << "\nCaught signal " << signum << ". Shutting down GPIO pins :)" << std::endl;
    // Cycle to shutting down all the pins
    for (int gpioPin = 0; gpioPin<=27; gpioPin++)
    {   digitalWrite(gpioPin, LOW); }
    // Terminate program
    exit(signum);
}

void createPWM(bool const moveFordware, float& DC){
    // Defining direction of rotation
    if (moveFordware){
        digitalWrite(ccwPin, HIGH);
        digitalWrite(cwPin, LOW);
    }else{
        digitalWrite(ccwPin, LOW);
        digitalWrite(cwPin, HIGH);
    }

    // Creating PWM
    digitalWrite(pwmPin, HIGH);
    float timeOn = DC/(100*freq);       // in [s]
    float timeOff = 1/freq - timeOn;    // in [s]
    usleep(timeOn*1'000'000);
    digitalWrite(pwmPin, LOW);
    usleep(timeOff*1'000'000);

    
}

int main() {
    // Register signal and signal handler used to shutting down all the pins when the program get closed
    signal(SIGINT, signal_callback_handler);    

    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

    pinMode(cwPin, OUTPUT);
    pinMode(ccwPin,OUTPUT);
    pinMode(pwmPin,OUTPUT);

    float DC = 0; // % of freq
    std::vector<float> dutyCycles;

    float DCsteps = 2.5; 
    int maxDC{50};
    int minDC{10};

    bool reverse = false;
    bool moveFordware=true;

    // Creation of DCs vector
    for (float dcs=minDC; dcs<=maxDC; dcs+=DCsteps){
        dutyCycles.push_back(dcs);
    }

    // Counter
    int i=0;

    while(1){
        if(reverse){
            i--;
        }else{
            i++;
        }

        DC = dutyCycles[i];

        // Cycle used to wait some time before changing duty-cycle, in order to have a gradual transition
        for (int j = 0; j<15; j++){
            createPWM(moveFordware, DC);
        }

        if (DC==dutyCycles.back() || DC==minDC){
            reverse = !reverse;
        }
    }
}