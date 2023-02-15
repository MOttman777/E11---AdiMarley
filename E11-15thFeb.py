import sys
import random
import time
import argparse

import csv
meta_data = ["Time","Random"]
f = open("random_data.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)
print(sys.argv)

unix = int(time.time())
timer = unix + 30

while unix < timer:
    unix = int(time.time())
    idata = random.random()
    print(unix,idata)
    time.sleep(1)
    data = [unix,idata]
    writer.writerow(data)

f.close()