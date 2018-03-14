import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(11,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)

check_1 = input("How many red lights in relay are ON?")
if check_1 != 0:
	print('Something is wrong, program ends.')
	exit()

def pump_on(pin_num,t):
	GPIO.output(pin_num,GPIO.LOW)
	time.sleep(t)
	GPIO.output(pin_num,GPIO.HIGH)

print("\033[1;33;40mTurn on 12V power and input time for each pump to start priming. Turn off 12V power when primed.")

time.sleep(1)
a = input("Time for PUMP_1:")
pump_on(11,a)

b = input("Time for PUMP_2:")
pump_on(13,b)

c = input("Time for PUMP_3:")
pump_on(15,c)

print("\033[0mDone. Place membranes and run produce.py")

GPIO.cleanup()


