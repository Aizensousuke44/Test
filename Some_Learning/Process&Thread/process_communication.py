import os
from random import random

import time

from multiprocessing import Queue, Process


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a', 'b', 'c', 'd']:
        print('Put %s into queue' % value)
        q.put(value)
        time.sleep(random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    # q.put([i for i in range(10)])
    # q.put('Hello')
    # print(q.get(True))
    # print(q.get(True))

