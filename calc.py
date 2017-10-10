from math import sqrt

def sum_proba(proba_res, nb):
    res = 0.0
    for x in range(10, 60, 10):
        for y in range(10, 60, 10):
            if x + y == nb:
                res += proba_res[x][y]
    return res;

def expected_val(law, start):
    mult = start
    res = 0
    for nb in law:
        res += nb * mult
        mult += 10
    return res

def variance(law, start):
    res = 0
    mult = start
    for nb in law:
        res += nb * ((mult - expected_val(law, start)) ** 2)
        mult += 10
    return res

def compute_proba(a, b, x, y):
    return (float((a - x) * (float(b) - y)) / float(((5 * a) - 150) * ((5 * b) - 150)))
