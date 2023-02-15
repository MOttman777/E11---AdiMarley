import sys
import random
import time
import argparse

start_time = time.time()
run_time = 10
itime = start_time

while itime < (start_time +run_time):
    itime = time.time()
    idata = random.random()
    print(itime,idata)
    time.sleep(1)

    