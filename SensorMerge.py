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