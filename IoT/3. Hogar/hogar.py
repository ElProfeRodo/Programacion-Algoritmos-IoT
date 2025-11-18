from gpio import *

def main():
	pinMode(0, OUT)
	pinMode(1, OUT)
	pinMode(2, OUT)
	pinMode(3, IN)
	pinMode(4, OUT)
	pinMode(5, OUT)
	
	while True:
		if digitalRead(3) == HIGH:
			customWrite(0, '2')
			customWrite(1, '1')
			customWrite(2, '2')
			customWrite(4, '1')
			digitalWrite(5, HIGH)
		else:
			customWrite(0, '0')
			customWrite(1, '0')
			customWrite(2, '0')
			customWrite(4, '0')
			digitalWrite(5, LOW)

if __name__ == "__main__":
	main()
