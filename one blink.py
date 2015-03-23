#!/usr/bin/env python

import gpio

def main():    
    
    pin39 = gpio.Gpio("13")
        
    pin39.direction("out")
    
    for i in range(1000):
        pin39.value("1")
    pin39.value("0")
    
    pin39.unexport()
    
if __name__ == "__main__":
    main()
    
