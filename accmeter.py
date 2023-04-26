import time
import board
import busio
import adafruit_adxl34x
import time
import argparse

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

import csv
meta_data = ["X","Y","Z"]
f = open(str(sys.argv[2]),"w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)
print(sys.argv)
start_time = int(time.time())
run_time = int(sys.argv[1])
itime = start_time

while itime < (start_time + run_time):
    print("%f %f %f"%accelerometer.acceleration)
    itime = int(time.time())
    try:
        accdata = accel.read()
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    data = [accdata[0],accdata[1],accdata[2]]
    writer.writerow(data)
f.close() 
    time.sleep(1)