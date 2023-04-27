#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
import argparse

rtime = int(sys.argv[1])
curtime = int(time.time())
ctime = int(time.time())

#GPIO pin set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# global variable
count = 0

# callback function defn
def count_pulse(channel):
    global count
    count += 1
    print(time.time())

# callback function
GPIO.add_event_detect(26, GPIO.FALLING, callback=count_pulse)

meta_data = ["Time","Count"]
f = open("radiation_count.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while ctime < curtime+rtime:
    ctime = int(time.time())
    try:
        count = 0
        time.sleep(60)
        print("Counts this minute:", count)
    except KeyboardInterrupt:
        # Clean up GPIO 
        GPIO.cleanup()
    data = [time.time(),count]
    writer.writerow(data)
    
f.close()

