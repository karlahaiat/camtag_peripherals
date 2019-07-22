#Script will turn on raspberry pi peripherals when button on GPIO 26 is pressed

import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
        input_state= GPIO.input(26)
	#If button is pressed, turn on usb peripherals and HDMI output
        if input_state== False:
                os.system("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/bind")
		sudo /opt/vc/bin/tvservice -p
