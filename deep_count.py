# Lists in lists

def deep_count(p):
    sum = 0
    for i in p:
        sum = sum + 1
        if isinstance(i, list):
            sum = sum + deep_count(i)
    return sum

print (deep_count([1, 2, 3]))
#>>> 3

# The empty list still counts as an element of the outer list
print (deep_count([1, [], 3]) )
#>>> 3

print (deep_count([1, [1, 2, [3, 4]]]))
#>>> 7

print (deep_count([[[[[[[[1, 2, 3]]]]]]]]))
#>>> 10