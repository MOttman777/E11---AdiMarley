import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

unix = int(time.time())
timer = unix + 30

reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)

print("Found PM2.5 sensor, reading data...")
meta_data = ["Time","pm10std", "pm25std", "pm100std"]
import csv
f = open("data.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while unix<timer:
    time.sleep(1)
    unix = int( time.time())
    t = time.localtime()
    print(t)
    try:
        aqdata = pm25.read()
        print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    data = [t,aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]
    writer.writerow(data)
    
f.close()
    
                                                                      
    