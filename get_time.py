import time

def time_execution(code):
    start = time.clock()
    #result = eval(code)
    code
    run_time = time.clock() - start
    return code, run_time

def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

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

def fibonacci_faster(num):
    current, after = 0, 1
    for i in range(0, num):
        current, after = after, current + after
    return current

cache = {}

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1


#print(time_execution(fibo(30)))
#print(time_execution(cached_execution(cache, cached_fibo, 140)))
#print(time_execution(cached_execution(cache, cached_fibo, 30)))
print(time_execution(cached_execution(cache, cached_fibo, 360)))

#print(time_execution(fibonacci_faster(236)))