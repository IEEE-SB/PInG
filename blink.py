#!/usr/bin/env python
import time
import gpio

def main():    
    
    pin39 = gpio.Gpio("13")
    pin39.direction("out")

    while True:
	 pin39.value("HIGH")
	 time.sleep(1)
	 pin39.value("LOW")
	 time.sleep(1)
    
    pin39.unexport()
    
if __name__ == "__main__":
    main()