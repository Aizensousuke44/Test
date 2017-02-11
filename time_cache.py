#To caculate the running time 
import time
def time_execution(code):
    start = time.clock()
    # result = eval(code)
    code
    run_time = time.clock() - start
    return code, run_time
    
#Make the program faster
def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]
#Example
def cached_fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return (cached_execution(cache, cached_fibo, (n - 1)) +
                cached_execution(cache, cached_fibo, (n - 2)))

def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


cache = {}
