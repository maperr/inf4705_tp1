# coding=utf-8
# using python 2.6+
import random
import time
import numpy
import csv
import sys
sys.setrecursionlimit(5000000)
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


# sample call: python algo.py (counting|quick|quickRandom|quickSeuil|quickRandomSeuil) (numdufichier.txt) (printResults(1/0)) (printTime(1/0))
# les calls arrivent comme ca
#   argv[1]: counting|quick|quickRandom|quickSeuil|quickRandomSeuil
#   argv[2]: numdufichier.txt
#   argv[3]: -p ou -t
#   argv[4]: -p ou -t
# def main():
#     # command line arguments version
#     with open(sys.argv[2]) as f:
#         arr = []
#         for line in f:
#             arr.append(int(line))
#     seuil = 20
#     start_time = time.time()
#     if sys.argv[1] == "counting":
#         arr = countingSort(arr)
#     elif sys.argv[1] == "quick":
#         arr = quickSortPivotFirst(arr)
#     elif sys.argv[1] == "quickRandom":
#         arr = quickSortPivotRandom(arr)
#     elif sys.argv[1] == "quickSeuil":
#         arr = quickSortPivotFirstSeuil(arr, seuil)
#     elif sys.argv[1] == "quickRandomSeuil":
#         arr = quickSortPivotRandomSeuil(arr, seuil)
#     elapsed_time = time.time() - start_time
#
#     t = False
#     p = False
#     for x in sys.argv:
#         if(x == '-t' or x == '--time'):
#             t = True
#         if(x == '-p' or x == '--print'):
#             p = True
#     if p == True:
#         for x in arr:
#             print(x)
#     if t == True:
#         print('Temps: {0} secondes.'.format(elapsed_time))

def main():
    resultsfilename = 'results50000-serie1.csv'
    with open(resultsfilename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        testsets = ['50000', '100000', '500000']

        # pour chaque testset
        for x in range(0, 10):
            filename = 'INF4705_H17_TP1_donnees/testset_50000_' + str(x) + '.txt'
            with open(filename) as f:
                arr = []
                for line in f:
                    arr.append(int(line))
            seuil = 20

            start_time_countingsort = time.time()
            countingSort(arr)
            end_time_countingsort = time.time()
            elapsed_time_countingsort = end_time_countingsort - start_time_countingsort

            start_time_quicksortpivotfirst = time.time()
            quickSortPivotFirst(arr)
            end_time_quicksortpivotfirst = time.time()
            elapsed_time_quicksortpivotfirst = end_time_quicksortpivotfirst- start_time_quicksortpivotfirst

            start_time_quicksortpivotfirstseuil = time.time()
            quickSortPivotFirstSeuil(arr, seuil)
            end_time_quicksortpivotfirstseuil = time.time()
            elapsed_time_quicksortpivotfirstseuil = end_time_quicksortpivotfirstseuil - start_time_quicksortpivotfirstseuil

            elapsed_time_quicksortpivotrandoms = 0
            elapsed_time_quicksortpivotrandomseuils = 0
            for y in range (0,10):
                start_time_quicksortpivotrandom = time.time()
                quickSortPivotRandom(arr)
                end_time_quicksortpivotrandom = time.time()
                elapsed_time_quicksortpivotrandom = end_time_quicksortpivotrandom - start_time_quicksortpivotrandom
                elapsed_time_quicksortpivotrandoms = elapsed_time_quicksortpivotrandoms + elapsed_time_quicksortpivotrandom

                start_time_quicksortpivotrandomseuil = time.time()
                quickSortPivotRandomSeuil(arr, seuil)
                end_time_quicksortpivotrandomseuil = time.time()
                elapsed_time_quicksortpivotrandomseuil = end_time_quicksortpivotrandomseuil - start_time_quicksortpivotrandomseuil
                elapsed_time_quicksortpivotrandomseuils = elapsed_time_quicksortpivotrandomseuils + elapsed_time_quicksortpivotrandomseuil

            elapsed_time_quicksortpivotrandoms = elapsed_time_quicksortpivotrandoms / 10
            elapsed_time_quicksortpivotrandomseuils = elapsed_time_quicksortpivotrandomseuils / 10

            spamwriter.writerow([filename, elapsed_time_countingsort, elapsed_time_quicksortpivotfirst, elapsed_time_quicksortpivotfirstseuil,elapsed_time_quicksortpivotrandoms, elapsed_time_quicksortpivotrandomseuils])

if __name__ == "__main__":
    main()
