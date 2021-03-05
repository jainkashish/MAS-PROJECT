from characteristic_function import *
from main import *

v = characteristic_fun(n)

final_coalition = []
discard = set()

def calculate_si(i):
    value = 0
    optimal = set()
    for key, val in v.items():
        if i in key and len(key.intersection(discard)) == 0:
            if (v[key]/len(key) > value):
                optimal = key
                value = v[key]/len(key)
    return value, optimal

def find_coalition(i):
    val = 0
    optimal = set()
    for x in range(n):
        t_val, t_optimal = calculate_si(x)
        if (t_val > val):
            val = t_val
            optimal = t_optimal

    for x in optimal:
        discard.add(x)
    final_coalition.append(optimal)


def find_optimal_coalition(n):
    for i in range(0, n) and i not in discard:
        find_coalition(i)
    return final_coalition
