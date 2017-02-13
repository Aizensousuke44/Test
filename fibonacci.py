def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_faster(num):
    current, after = 0, 1
    for i in range(0, num):
        current, after = after, current + after
    return current

#print(fibonacci(36))
print(fibonacci_faster(136))