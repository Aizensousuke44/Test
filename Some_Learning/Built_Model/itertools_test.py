import itertools

''' iterator '''
# Start from 5
natuals = itertools.count(5)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for item in itertools.chain('bnv', '123', 'HFK'):
    print(item)

for m, n in itertools.groupby('BbbGgHhhhJjjjKk', lambda x: x.upper()):
    print(m, list(n))