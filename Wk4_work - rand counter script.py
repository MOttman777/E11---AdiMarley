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

start_time = int(time.time())
run_time = int(sys.argv[1])
itime = start_time

while itime < (start_time + run_time):
    itime = int(time.time())
    idata = random.random()
    print(itime,idata)
    time.sleep(1)
    data = [itime,idata]
    writer.writerow(data)

    