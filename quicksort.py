from random import randint


def quickSort(L, ascending=True):
    if len(L) <= 1:
        return L
    smaller, equal, larger = [], [], []
    pivot = L[randint(0, len(L) - 1)]

    for x in L:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    larger = quickSort(larger, ascending=ascending)
    smaller = quickSort(smaller, ascending=ascending)

    if ascending:
        final = smaller + equal + larger
    else:
        final = larger + equal + smaller
    return final


l2 = list([3.14159 , 1./127, 2.718 , 1.618 , -23., 3.14159])
print(quickSort(l2, ascending=False))
# [3.14159, 3.14159, 2.718, 1.618, 0.007874015748031496, -23.0]