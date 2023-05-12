"""1 Use multiprocessing to create three separate processes.
 Make each one wait a random number of seconds between zero and one,
print the current time, and then exit.
"""
import multiprocessing
from random import random
import os
import time


def timewait():
    time.sleep(random())
    print ("Time: ", time.strftime("%H:%M:%S"))

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=timewait)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


