import pickle

d = dict(name='Joker', age=24, enemy='Society', phone=None)

with open('dump.txt', 'wb') as file_:
    pickle.dump(d, file_)

with open('dump.txt', 'rb') as file_:
    dd = pickle.load(file_)

print(dd)

import json

# to standard json
dd1 = json.dumps(dd)
print(dd1)

dd2 = json.loads(dd1)
print(dd2)