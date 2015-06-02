#!/usr/bin/env python

import gpio

def main():    
    
    pin39 = gpio.Gpio("13")
        
    pin39.direction("out")
    
    for i in range(1000):
        pin39.value("HIGH")
    pin39.value("LOW")
    
    pin39.unexport()
    
if __name__ == "__main__":
    main()
    
