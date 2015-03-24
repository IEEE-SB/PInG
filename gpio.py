#!/usr/bin/env python
#
#

# Galileo pins (digital and analog)
dir = { "0" : "50",
        "1" : "51",
        "2" : "32",
        "3" : "18",
        "4" : "28",
        "5" : "17",
        "6" : "24",
        "7" : "27",
        "8" : "26",
        "9" : "19",
        "10": "16",
        "11": "25",
        "12": "38",
        "13": "39",
        "A0": "37",
        "A1": "36",
        "A2": "23",
        "A3": "22",
        "A4": "21",
        "A5": "20"
    }


class Gpio:
    
    def __init__(self, pin):
        self.pin = dir[pin]        
        self.export(self.pin)        

    def wfifo(self,file,data):
        self.fifo = open(file,"w")
        self.fifo.write(data)
        self.fifo.close()

    def get_rfifo(self):
        for key in dir.keys() :
            if self.pin == dir[key]:
                x = key.split('A')
                c = x[1]       
        self.file = = '/sys/bus/iio/devices/iio:device0/in_voltage'+str(c)+'_raw'
        self.fifo = open(self.file,"r")
        self.a = self.fifo.read()
        self.fifo.close()
        return self.a

    def export(self,pin):
        self.wfifo("/sys/class/gpio/export", self.pin)

    def direction(self,dir):
        self.wfifo("/sys/class/gpio/gpio%s/direction" %self.pin, dir)

    def value(self,value):
        self.wfifo("/sys/class/gpio/gpio%s/value" %self.pin,value)

    def unexport(self):
        self.wfifo("/sys/class/gpio/unexport", self.pin)
        
