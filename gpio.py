#!/usr/bin/env python
#
#

# Galileo pins (digital and analog)
dir = { "0" : "50",
        "1" : "51",
        "2" : "32",
        "3" : "3",
        "4" : "28",
        "5" : "5",
        "6" : "6",
        "7" : "27",
        "8" : "26",
        "9" : "1",
        "10": "7",
        "11": "4",
        "12": "38",
        "13": "39",
        "A0": "37",
        "A1": "36",
        "A2": "23",
        "A3": "22",
        "A4": "21",
        "A5": "20"
    }

# Galileo pwm pins
dir_pwm = { "3" : "3",
            "5" : "5",
            "6" : "6",
            "9" : "1",
            "10": "7",
            "11": "4",
}

class Gpio:

    def __init__(self, pin):
        self.pin = dir[str(pin)]
        self.export()
        self.pwm_pin = self.ispwm()
    
    def ispwm(self):
        return (True if self.pin in dir_pwm.values() else False)
    
    def wfifo(self, file, data):
        self.fifo = open(file,"w")
        self.fifo.write(data)
        self.fifo.close()

    def get_rfifo(self):
        for key in dir.keys() :
            if self.pin == dir[key]:
                x = key.split('A')
                c = x[1]       
        self.file = '/sys/bus/iio/devices/iio:device0/in_voltage'+str(c)+'_raw'
        self.fifo = open(self.file,"r")
        self.a = self.fifo.read()
        self.fifo.close()
        return self.a

    # duty_cycle: 0-100%
    # nanoseconds: default 1000000 
    def pwm(self, duty_cycle, nanoseconds):
        duty_cycle = self.get_value(duty_cycle)
        self.wfifo("/sys/class/pwm/pwmchip0/pwm%s/period" %self.pin, nanoseconds)
        self.wfifo("/sys/class/pwm/pwmchip0/pwm%s/duty_cycle" %self.pin, duty_cycle)

    def export(self):
        if self.pin in dir_pwm.values():
            self.wfifo("/sys/class/pwm/pwmchip0/export", self.pin)           
            self.wfifo("/sys/class/pwm/pwmchip0/pwm%s/enable" %self.pin, "1")
        else:
            self.wfifo("/sys/class/gpio/export", self.pin)
            
    def direction(self, dir):
        self.wfifo("/sys/class/gpio/gpio%s/direction" %self.pin, dir)

    def value(self, value, nanoseconds = "1000000"):
        value = str(value)
        if self.pwm_pin == True:
            self.pwm(value, nanoseconds)
        else:
            if value == "HIGH":
                value = "1"
            else:
                value = "0"
            self.wfifo("/sys/class/gpio/gpio%s/value" %self.pin,value)

    def get_value(self, duty_cycle):
        if not duty_cycle.isdigit():
            if duty_cycle == "HIGH":
                duty_cycle = "1000000"
            else:
                duty_cycle = "0"
        else:
            duty_cycle = int("1000000")*int(duty_cycle)/100
        return str(duty_cycle)

    def unexport(self):
        if not self.pwm_pin:
            self.wfifo("/sys/class/gpio/unexport", self.pin)    
        else:    
            self.wfifo("/sys/class/pwm/pwmchip0/pwm%s/enable" %self.pin, "0")
            self.wfifo("/sys/class/pwm/pwmchip0/unexport", self.pin)
