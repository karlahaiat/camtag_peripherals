import time
import threading
import os

def startprgm(i):
    	if (i == 0):
        	os.system("sudo python /home/pi/magnet.py")
    	elif (i == 1):
        	os.system("sudo python /home/pi/sensors/gpsser.py")
	elif (i == 2):
		os.system("sudo python /home/pi/sensors/accelerometer.py")
	elif (i ==3):
		os.system("sudo python /home/pi/sensors/light.py")
	elif (i ==4):
                os.system("sudo python /home/pi/sensors/keller.py")
	#elif (i ==5):
         #       os.system("sudo python /home/pi/camera.py")
          #      print "6"
	else:
        	pass

for i in range(5):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()
