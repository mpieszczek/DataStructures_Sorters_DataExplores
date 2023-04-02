from sorters import merge_sort as merge_sort


def binary_select(array, k):
    i = 0
    j = len(array) - 1
    while i <= j:
        m = i + j // 2
        if array[m] > k:
            j = m - 1
        elif array[m] < k:
            i = m + 1
        else:
            return True, m
    return False


def _median5(array):
    array_copy = array.copy()
    merge_sort(array_copy)
    if len(array_copy) % 2 == 0:
        return array_copy[len(array_copy) // 2 - 1]
    else:
        return array_copy[len(array_copy) // 2]


def _pivot(array):
    # get median of medians
    if len(array) < 5:
        return _median5(array)
    # get medians
    medians = []
    left, right = 0, 5
    while left < len(array):
        temp = array[left:right]
        # print(temp)
        medians.append(_median5(temp))
        left, right = left + 5, right + 5
    # get median of medians
    return _median5(medians)


def _partition(array, p):
    l, m, r = [], [], []
    for a in array:
        if a < p:
            l.append(a)
        elif a > p:
            r.append(a)
        else:
            m.append(a)
    return l, m, r


def select(array, k):
    # returns k statistic from sorted array
    piv = _pivot(array)
    l, m, r = _partition(array, piv)
    if len(l) - 1 >= k:
        return select(l, k)
    elif len(l) + len(m) <= k:
        return select(r, k - len(l) - len(m))
    else:
        return m[0]
