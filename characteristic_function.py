import itertools
v = {}

num = []


def getSubsets(n):
    for x in range(1, n+1):
        num.append(x)
    for t in range(1, n+1):
        for x in list(itertools.combinations(num, t)):
            v[x] = 0


def characteristic_fun(n):
    getSubsets(n)  # it generates all subsets
    for key, val in v.items():
        sum = 0
        for x in key:
            sum += x
        v[key] = sum
    for key, val in v.items():
        print(key)
        print(val)
