#!/usr/bin/python
from kellerLD import KellerLD
import time
import os
from read_tsl import Tsl2591
from mpu6050 import mpu6050

debug=True

#Save data in data/pressure
directory = '/home/pi/newtest/tag_data/sensors/'
if not os.path.exists(directory):
        os.makedirs(directory)
text_file = open(directory + str(int(time.time())) + '.txt','w')
header="{0},{1},{2},{3},{4},{5},{6},{7}\n".format('UTC','Pressure','Temperature','Lux','IR spectrum','ax','ay','az')
print header
text_file.write(header)

sensor = KellerLD()
if not sensor.init():
        print "Failed to initialize Keller LD sensor!"
        exit(1)

tsl = Tsl2591()  # initialize

mpu = mpu6050(0x68)

while True:
        try:
                sensor.read()
                full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
        	lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
		ac = mpu.get_accel_data()
		X=(ac['x'])
		Y=(ac['y'])
		Z=(ac['z'])
		#gyro=mpu.get_gyro_data()
		#X=(gyro['x'])
                #Y=(gyro['y'])
                #Z=(gyro['z'])
		sensors="{0},{1},{2},{3},{4},{5},{6},{7}\n".format(str(time.time()),str(sensor.pressure()),str(sensor.temperature()),str(lux),str(ir),str(X),str(Y),str(Z))
		time.sleep(1)
		text_file.write(sensors)
		if lux > 1000:
			os.system("sudo shutdown now")
		if debug:
			print sensors

        except Exception as e:
                print e
