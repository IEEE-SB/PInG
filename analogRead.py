import time
import gpio

def main():
   pinA0 = gpio.Gpio("A0")
   pinA0.direction("out")
   pinA0.value("0")

   while True:
	time.sleep(1)
	a = pinA0.get_rfifo()
	print a


if __name__ == "__main__":
   main()
