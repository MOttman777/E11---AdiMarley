import sys
import random
import time
import argparse
import csv
import adafruit_bme680
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C


# Air Quality Sensor
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

# Weather Sensor
reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

import csv
meta_data = ["Time","PM10 std","PM25 std","PM 100 std","Temperature","Gas","Pressure","Altitude","Relative Humidity"]
f = open("random_data.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)
print(sys.argv)
start_time = int(time.time())
run_time = int(sys.argv[1])
itime = start_time

while itime < (start_time + run_time):
    itime = int(time.time())
    print("\nTemperature: %0.1f C" % bme680.temperature)
        print("Gas: %d ohm" % bme680.gas)
        print("Humidity %0.1f%%" % bme680.relative_humidity)
        print("Pressure %0.3f hPa" % bme680.pressure)
        print("Altitude = % 0.2f meters" % bme680.altitude)
    try:
        aqdata = pm25.read()
        print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    data = [itime,aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature,bme680.gas,bme680.pressure,bme680.altitude,bme680.relative_humidity]
    writer.writerow(data)
f.close()                             