from gpio import *

def main():
	pinMode(0, OUT)
	pinMode(1, IN)
	
	while True:
		if digitalRead(1) == HIGH:
			digitalWrite(0, HIGH)
		else:
			digitalWrite(0, LOW)

if __name__ == "__main__":
	main()