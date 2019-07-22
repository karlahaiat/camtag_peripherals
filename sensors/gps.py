#!/usr/bin/python
import sys
import os
import serial
import threading
import time

def gps():
        ser=serial.Serial(COMPORT,BAUDRATE,timeout=0)
	header="{0},{1},{2},{3},{4}\n".format('Date','GMT Time','UTC','North','West')
	#header1="Note that 4042.6142,N is (Latitude 40 degrees, 42.6142 decimal minutes North) & 07400.4168,W. (Longitude 74 degrees, 0.4168 decimal minutes West)\n"
	directory = '/home/pi/newtest/tag_data/GPS/'
	if not os.path.exists(directory):
        	os.makedirs(directory)
	text_file = open(directory + str(int(time.time())) + '.txt','w')
	text_file.write(header)
	#text_file.write(header)

        while True:
        	line=ser.readline()
                time.sleep(1)
		#print 'test'
		if "$GPRMC" in line:
                    data = line.split(',')
                    if data[2] == 'A':
                    	day = data[9][0:2]
                        month = data[9][2:4]
                        year = int(data[9][4:6]) + 2000
                        date = "%d-%s-%s" % (year, month, day)
                        hour = data[1][0:2]
                        min = data[1][2:4]
                        sec = data[1][4:6]
                        t = "%s:%s:%s" % (hour, min, sec)
                        #dateTime = "%s %s" % (date, t)
                        north = data[3]
                        west = data[5]
			gps="{0},{1},{2},{3},{4}\n".format(str(date),str(t),str(time.time()),str(north),str(west))
                        print gps
			text_file.write(gps)


COMPORT='/dev/serial0'
BAUDRATE=9600
gps()
