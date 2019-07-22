#!/usr/bin/python
from kellerLD import KellerLD
import time
import os
from read_tsl import Tsl2591
from mpu6050 import mpu6050

#Save data in data/pressure
directory = '/home/pi/newtest/all/'
if not os.path.exists(directory):
        os.makedirs(directory)
text_file = open(directory + str(int(time.time())) + '.txt','w')
header="{0},{1},{2},{3},{4},{5},{6},{7}\n".format('UTC','Pressure','Temperature','Lux','IR spectrum','x','y','z')
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
		#print ac
		pressure="{0},{1},{2},{3},{4},{5},{6},{7}\n".format(str(time.time()),str(sensor.pressure()),str(sensor.temperature()),str(lux),str(ir),str(X),str(Y),str(Z))
		#light= "{0},{1},{2},{3},{4},{5}\n".format(str(time.time()),str(lux),str(full),str(ir),str(sensor.pressure(),str(sensor.temperature()))
		time.sleep(1)
		print pressure
                text_file.write(pressure)


   # accel_data = mpu.get_accel_data()
   # print(accel_data['x'])
   # print(accel_data['y'])
   # print(accel_data['z'])
  #  gyro_data = mpu.get_gyro_data()
  #  print(gyro_data['x'])
  #  print(gyro_data['y'])
#    print(gyro_data['z'])




        except Exception as e:
                print e
