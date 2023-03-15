#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time
import datetime

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

while True:
    try:
        count = 0
        time.sleep(60)
        print("Counts this minute:", count)
    except KeyboardInterrupt:
        # Clean up GPIO 
        GPIO.cleanup()

