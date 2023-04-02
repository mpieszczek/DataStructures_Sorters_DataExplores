from math import floor


def insert_sort(array):
    if len(array) == 0:
        return []
    result = [None]
    for i in range(len(array)):
        result.append(None)
        result[0] = array[i]
        k = len(result) - 1
        while k > 0:
            k -= 1
            if array[i] < result[k]:
                result[k + 1] = result[k]
                result[k] = None
            else:
                result[k + 1] = array[i]
                break
    return result[1:]


def radix_sort(array):
    maks = max(array)
    digit = len(str(maks))
    return _radix_sort(array, digit)


def _radix_sort(array, digit):
    if digit == -1:
        return array
    if len(array) <= 1:
        return array
    buckets = [[] for i in range(10)]
    for i in range(len(array)):
        buckets[array[i] // 10 ** digit % 10].append(array[i])
    for i in range(10):
        buckets[i] = _radix_sort(buckets[i], digit - 1)
    result = []
    for b in buckets:
        result += b
    return result


def bucket_sort(array, k=10, next_sort=insert_sort):
    buckets = [[] for i in range(k)]
    maks = max(array)
    for i in range(len(array)):
        buckets[floor((k - 1) * array[i] / maks)].append(array[i])
    for i in range(k):
        buckets[i] = next_sort(buckets[i])
    result = []
    for b in buckets:
        result += b
    return result


def merge_sort(array):
    s = 1
    while s < len(array):
        s *= 2
        k = -s
        l = 0
        while l < len(array):
            k += s
            l += s
            sr = (k + l) // 2
            _scalanie(array, sr, k, l)
    return 0


def _scalanie(tab, m, k, l):
    # opcjonalne pomagają przy iteracyjnym zapobiegają wyjścia poza iterator
    # przy rekurencyjnym są zbędne
    l = min(l, len(tab))
    m = min(m, len(tab))
    # zakladamy ze elementy w częściahc k-m oraz m-l są posortowane
    i = k
    j = m
    # tablica wyjściowa - jest to posortowany fragment tab od k do l
    B = []
    # indeksujemy po oby polówkach i dodajemy do B element mniejszy
    while i < m and j < l:
        if tab[i] <= tab[j]:
            B.append(tab[i])
            i += 1
        else:
            B.append(tab[j])
            j += 1
    # skonczyly się elementy z 2 polowki
    while i < m:
        B.append(tab[i])
        i += 1
    # skonczyly się elementy z 1 polowki
    while j < l:
        B.append(tab[j])
        j += 1
    # nadpisz fragment wejściowej tablicy
    tab[k:l] = B
    return 0


def quick_sort(array):
    #TO DO
    return array
