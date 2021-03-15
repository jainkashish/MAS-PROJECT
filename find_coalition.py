import characteristic_function

v = {}

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


def find_coalition(n):
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
    v = characteristic_function.characteristic_fun(n)
    # for key, val in v.items():
    #     for j in key:
    #         print(j)
    #     print("----------------------")
    while(len(discard) != n):
        find_coalition(n)
    return final_coalition
