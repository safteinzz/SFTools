# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:49:15 2020

@author: SaFteiNZz
"""

from queue import Queue
from threading import Thread

def do_stuff(q):
  while True:
    print(q.get())
    q.task_done()

q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  q.put(x)

q.join()