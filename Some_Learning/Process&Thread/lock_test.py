
import time, threading

balance = 0

lock = threading.Lock()

def change_it(n):
    global balance
    balance += 5
    balance -= 5

def run_thread(n):
    for _ in range(1000):
        # lock on
        lock.acquire()
        try:
            change_it(n)
        finally:
            # lock off
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance)