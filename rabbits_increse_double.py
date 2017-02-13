def rabbits(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)

print (rabbits(10))
#>>> 35

s = ""
for i in range(1,12):
    s = s + str(rabbits(i)) + " "
print (s)
#>>> 1 1 2 3 5 7 11 16 24 35 52