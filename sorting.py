import numpy as np
from numpy.random import default_rng

def swap(a, n, m):
    """ Swap n'th element in array a with m'th """
    tmp = a[n]
    a[n] = a[m]
    a[m] = tmp

def find_smallest(a, p):
    """Find the smallest element in an array a recursivly"""
    if len(a)-1 == p:
        return p 
    s = find_smallest(a, p+1)
    return p if a[p] < a[s] else s


def selection_sort(a, b):
    if len(a) == 1:
        b.append(a[0])
    else:
        s = find_smallest(a, 0)
        b.append(a[s])
        swap(a, s, 0) 
        selection_sort(a[1:], b)
     
def quick_sort(a,start,end):
    """Sorting a in place using quick sort algorithm"""
    if end-start > 0:
        boundary = start
        for i in range(start+1,end+1):
            if a[i] < a[boundary]:
                boundary += 1
                swap(a, i, boundary)
                swap(a, boundary-1, boundary)
        quick_sort(a, start, boundary)
        quick_sort(a, boundary+1, end)
        
    
rng = default_rng()
a = rng.integers(low=1, high=100, size=10)
print(a)
quick_sort(a, 0, len(a)-1)
print(a)
