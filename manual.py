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
input("Please turn on the 12 V power for all pumps, to confirm input 1:")

time.sleep(1)
a = input("Time for PUMP_1:")
GPIO.output(11,GPIO.LOW)
time.sleep(a)
GPIO.output(11,GPIO.HIGH)

b=input("Time for PUMP_2:")
GPIO.output(13,GPIO.LOW)
time.sleep(b)
GPIO.output(13,GPIO.HIGH)

c=input("Time for PUMP_3:")
GPIO.output(15,GPIO.LOW)
time.sleep(c)
GPIO.output(15,GPIO.HIGH)

print("Done")

GPIO.cleanup()


