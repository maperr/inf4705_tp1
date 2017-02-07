# coding=utf-8
# using python 2.6+
import random
import sys
import time
import numpy

# seuil optimal est 20

# pris de http://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#Python
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


# pris de http://rosettacode.org/wiki/Sorting_algorithms/Counting_sort#Python
def countingSort(array):
    maxval = max(array)
    m = maxval + 1
    count = numpy.bincount(array)
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1

    return array

# pris de http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSortPivotFirst(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSortPivotFirst(less)
        more = quickSortPivotFirst(more)
        return less + pivotList + more


# inspiré de http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSortPivotRandom(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        index = random.randint(0, len(arr) - 1)
        pivot = arr[index]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSortPivotRandom(less)
        more = quickSortPivotRandom(more)
        return less + pivotList + more


# inspiré de http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSortPivotFirstSeuil(arr, seuil):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        if len(less) >= seuil:
            less = quickSortPivotFirstSeuil(less, seuil)
        else:
            insertion_sort(less)
        if len(more) >= seuil:
            more = quickSortPivotFirstSeuil(more, seuil)
        else:
            insertion_sort(more)
        return less + pivotList + more


# inspiré de http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSortPivotRandomSeuil(arr, seuil):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        index = random.randint(0, len(arr) - 1)
        pivot = arr[index]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        if len(less) >= seuil:
            less = quickSortPivotRandomSeuil(less, seuil)
        else:
            insertion_sort(less)
        if len(more) >= seuil:
            more = quickSortPivotRandomSeuil(more, seuil)
        else:
            insertion_sort(more)
        return less + pivotList + more

def printArray(arr):
    print '\n'.join(str(p) for p in arr)


# sample call: python algo.py (counting|quick|quickRandom|quickSeuil|quickRandomSeuil) (numdufichier.txt) (printResults(1/0)) (printTime(1/0))
def main():
    # command line arguments version
    with open(sys.argv[2]) as f:
        arr = []
        for line in f:
            arr.append(int(line))
    seuil = 20
    t0 = time.time()
    if sys.argv[1] == "counting":
        arr = countingSort(arr)
    elif sys.argv[1] == "quick":
        arr = quickSortPivotFirst(arr)
    elif sys.argv[1] == "quickRandom":
        arr = quickSortPivotRandom(arr)
    elif sys.argv[1] == "quickSeuil":
        arr = quickSortPivotFirstSeuil(arr, seuil)
    elif sys.argv[1] == "quickRandomSeuil":
        arr = quickSortPivotRandomSeuil(arr, seuil)

    # trouver temps sans seuil
    t1 = time.time()
    total1 = t1 - t0

    if(sys.argv[3] == '1'):
        for x in arr:
            print(x)

    if(sys.argv[4] == '1'):
        print('Elapsed time:' + total1 + ' s')

if __name__ == "__main__":
    main()
