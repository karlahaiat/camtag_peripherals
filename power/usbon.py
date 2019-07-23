#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(26, GPIO.FALLING, callback=send, bouncetime=300)

def send(channel):
	os.system("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/bind")
	#os.system("sudo /opt/vc/bin/tvservice -p")

setup()

while True:
    time.sleep(6000)
