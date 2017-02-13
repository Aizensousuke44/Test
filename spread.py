# Spread something,
# like one person spread a news to some people,
# and these people should told the same count of people different by own.

# n is the count of got news person,
# spread means one person should let the count(spread) of person to know
# target is the count of person knew news.

def hexes_to_udaciousness(n, spread, target):
    result = n + (n * spread)
    if n >= target:
        return 0
    else:
        return hexes_to_udaciousness(result, spread, target) + 1



print(hexes_to_udaciousness(100000, 2, 36230))
# >>> 0

print(hexes_to_udaciousness(50000, 2, 150000))
# >>> 1

print(hexes_to_udaciousness(50000, 2, 150001))
# >>> 2

print(hexes_to_udaciousness(20000, 2, 7 * 10 ** 9))
# >>> 12

print(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9))
# >>> 10