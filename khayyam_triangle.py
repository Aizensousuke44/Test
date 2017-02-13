def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        
# Former codes were coded for last codes
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
        
''' From http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000'''

# Now, the way is straight with argument
def make_next_row(row):
    result = []
    prev = 0
    for i in row:
        result.append(i + prev)
        prev = i
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = make_next_row(current)

    return result

print(triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
