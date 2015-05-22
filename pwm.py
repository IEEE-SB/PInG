# !/usr/bin/env python

# Increase/Decrease the brightness

import gpio
import time

def main():
    
    pin9 = gpio.Gpio(9)
    
    for i in range(10):
        pin9.value(i*10)
        time.sleep(0.5)
        
    for i in range(10):
        pin9.value(100-i*10)
        time.sleep(0.5)
    
    pin9.unexport()
    
if __name__ == "__main__":
    main()
