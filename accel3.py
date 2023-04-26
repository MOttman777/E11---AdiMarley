#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import sys
import time
import board
import busio
import adafruit_lis3dh
import csv

if hasattr(board, "ACCELEROMETER_SCL"):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
else:
    i2c = board.I2C()
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_4_G

meta_data = ["X","Y","Z"]
f = open(str(sys.argv[2]),"w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)
print(sys.argv)
start_time = int(time.time())
run_time = int(sys.argv[1])
itime = start_time

# Loop forever printing accelerometer values
while itime < (start_time + run_time):
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.  Divide them by 9.806 to convert to Gs.
    x, y, z = [
        value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration
    ]
    print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    adata = [x, y, z]
    writer.writerow(adata)
    itime = int(time.time())
    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.1)
f.close()

