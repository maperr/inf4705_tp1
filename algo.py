# coding=utf-8
# using python 2.6+
import random
import sys
import time
import matplotlib.pyplot as plt
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
def countingSort(alist):
    maximum = max(alist)
    minimum = min(alist)
    counting_alist = [0] * (maximum - minimum + 1)

    for i in alist:
        counting_alist[i - minimum] += 1

    sorted_alist = []
    for i in range(minimum, maximum + 1):
        if counting_alist[i - minimum] > 0:
            for j in range(0, counting_alist[i - minimum]):
                sorted_alist.append(i)

    return sorted_alist


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


# sample call: python quicksort.py (numdufichier.txt) (counting|quick|quickRandom|quickSeuil|quickRandomSeuil)
def main():
    # command line arguments version
    # with open(sys.argv[1]) as f:
    #     arr = []
    #     for line in f:
    #         arr.append(int(line))
    # t0 = time.time()
    # if sys.argv[2] == "counting":
    #     arr = countingSort(arr)
    # elif sys.argv[2] == "quick":
    #     arr = quickSortPivotFirst(arr)
    # elif sys.argv[2] == "quickRandom":
    #     arr = quickSortPivotRandom(arr)
    # elif sys.argv[2] == "quickSeuil":
    #     arr = quickSortPivotFirstSeuil(arr, seuil)
    # elif sys.argv[2] == "quickRandomSeuil":
    #     arr = quickSortPivotRandomSeuil(arr, seuil)


    # edit file to open
    with open("INF4705_H17_TP1_donnees/testset_100000_0.txt") as f:
        arr = []
        for line in f:
            arr.append(int(line))
    # t0 = time.clock()
    # edit algo. to use
    # arr = countingSort(arr)
    # arr = quickSortPivotFirst(arr)
    # arr = quickSortPivotFirstSeuil(arr, seuil)
    # arr = quickSortPivotRandom(arr)
    # arr = quickSortPivotRandomSeuil(arr, seuil)

    # trouver temps sans seuil
    t2 = time.clock()
    quickSortPivotFirst(arr)
    t3 = time.clock()
    total1 = t3 - t2
    print(total1)

    # trouver temps avec seuil
    tempsmin = -1
    seuilmin = -1
    seuil = 0
    while seuil < 100:
        t0 = time.clock()
        quickSortPivotFirstSeuil(arr, seuil)
        t1 = time.clock()
        total2 = t1 - t0
        if total2 < tempsmin or tempsmin == -1:
            seuilmin = seuil
            tempsmin = total2
        print '{0:10} -- {1:10} -- {2:10}, current min: {3:10}'.format(seuil, total2, total1, seuilmin)
        seuil += 1


if __name__ == "__main__":
    main()