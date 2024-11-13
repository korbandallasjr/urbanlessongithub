from math import inf


def divide(first, second):
    res = ''
    if second == 0:
        return inf
    else:
        res = float(first) / float(second)
        return res
