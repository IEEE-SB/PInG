import time
import gpio

def main():
   pinA0 = gpio.Gpio("A0")
   pinA0.direction("out")
   pinA0.value("0")

   for i in range(10):
	time.sleep(1)
	a = pinA0.get_value()
	print a
   
   pinA0.unexport()   

if __name__ == "__main__":
   main()
