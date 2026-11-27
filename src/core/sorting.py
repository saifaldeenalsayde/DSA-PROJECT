def length(a):
    count = 0
    for _ in a:
        count += 1
    return count

def less(v, w):
    return v < w

def exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap

def selection_sort(a):
    n = length(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if less(a[j], a[min_idx]):
                min_idx = j
        exch(a, i, min_idx)
    return a

def insertion_sort(a):
    n = length(a)
    for i in range(n):
        for j in range(i, 0, -1):
            if less(a[j], a[j - 1]):
                exch(a, j, j - 1)
            else:
                break
    return a

def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi + 1):
        aux[k] = a[k]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif less(aux[j], aux[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def sort_recursive(a, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    sort_recursive(a, aux, lo, mid)
    sort_recursive(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)

def merge_sort(a):
    n = length(a)
    aux = [None] * n
    sort_recursive(a, aux, 0, n - 1)
    return a