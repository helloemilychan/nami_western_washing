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

print("\033[1;33;40m####################################################")
print("#####      Nami Automatic Western Washer       #####")
print("#####                Ver 1.14                  #####")
print("#####            Updated 2/28/2018             #####")
print("####################################################")
print("\033[1;34;40m               by Dr. Yunkai Zhang                  ")

def pump_on(pin_num,t):
	GPIO.output(pin_num,GPIO.LOW)
	time.sleep(t)
	GPIO.output(pin_num,GPIO.HIGH)

print("\033[0;35;40mInput parameters:")
check_1 = input("\033[0mHow many red lights in relay are ON?")
if check_1 != 0:
	print('Something is wrong, program ends.')
	exit()
input("Please turn on the 12 V power for all pumps, to confirm input 1:")
a = input("How many times washing?")
b = input("Washing time (in minutes)?")
c = input("2nd Antibody incubation time? (in minutes)")
d = input("Pause time (min) before/after 2nd Antibody incubation\n")

#print("This is a test script with short time setting.")
time.sleep(1)
for i in range(1,a+1):
	s = '\033[0;36;40mWashing_{times}.'
	print(s.format(times=i))
	pump_on(11,30)
	time.sleep(b*60)
	pump_on(15,90)
	time.sleep(1)
if d > 0:
	pump_on(11,30)
	print("Removing membrane from tray")
	time.sleep(d*60)
	pump_on(15,90)

print("Adding 2nd Antibody")
pump_on(13,90)
time.sleep(c*60)
pump_on(15,180)

for i in range(1,a+1):
	s2 = 'Washing_{times} after 2nd Antibody.'
	print(s2.format(times=i))
	pump_on(11,30)
	time.sleep(b*60)
	pump_on(15,90)

print("\033[1;31;40mProcess Done")
print("\033[0mAdding TBST to keep membrane until visualize")
pump_on(11,30)

GPIO.cleanup()


