from gpio import *
from time import sleep

def main():
	pinMode(0, OUT)
	pinMode(1, OUT)
	pinMode(2, OUT)
	pinMode(3, OUT)
	
	pin0 = 0
	pin1 = 1
	pin2 = 2
	pin3 = 3
	
	while True:
		digitalWrite(pin0, HIGH)
		digitalWrite(pin1, LOW)
		digitalWrite(pin2, LOW)
		digitalWrite(pin3, LOW)
		
		aux = pin3
		pin3 = pin2
		pin2 = pin1
		pin1 = pin0
		pin0 = aux
		
		sleep(1)

if __name__ == "__main__":
	main()