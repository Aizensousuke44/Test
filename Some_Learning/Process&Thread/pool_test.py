import os, random, time
from multiprocessing import Pool

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    used = time.time() - start
    print('Task %s ran %0.2f seconds' % (name, used))

def pool_test(size, num, func):
    from contextlib import closing
    with closing(Pool(size)) as p:
        for i in range(num):
            p.apply_async(func, args=(i,))
        print('Waiting for all subprocess done')
    p.join()
    print('All subprocesses done')

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    # p = Pool(5)
    # for i in range(20):
    #     p.apply_async(long_time_task, args=(i,))
    # print('Waiting for all subprocess done')
    # p.close()
    # p.join()
    # print('All subprocesses done')
    pool_test(5, 20, long_time_task)
