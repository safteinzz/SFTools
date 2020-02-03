# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:26:15 2020

@author: SaFteiNZz
"""

import threading, time, random
from queue import Queue

jobs = Queue()

def do_stuff(q):
    while not q.empty():
        value = q.get()
        time.sleep(4)
        print(value)
        q.task_done()

for i in range(10):
    jobs.put(i)

for i in range(3):
    print('assssssss')
    worker = threading.Thread(target=do_stuff, args=(jobs,))
    worker.start()

print("waiting for queue to complete", jobs.qsize(), "tasks")
jobs.join()
print("all done")