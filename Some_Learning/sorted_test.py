
def by_name(l):
    return l[0][0]

def by_score(l):
    return l[1]

if __name__ == '__main__':
    L = [('Bob', 75), ('Allen', 92), ('Chris', 66), ('Lee', 88)]

    L1 = sorted(L, key=by_name)
    print(L1)

    L2 = sorted(L, key=by_score)
    print(L2)