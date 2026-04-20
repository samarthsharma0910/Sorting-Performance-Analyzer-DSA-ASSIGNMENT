# Assignment 3
# Sorting Performance Analyzer (SPA)

'''Name of the School: School of Engineering & Technology
Program (Class / Semester / Batch): B.Tech CSE (AI & ML) , 2nd semester, 2025-29
Course Title: Data Structures
Course Code: ETCCDS202
Unit Number: 3
Unit Title: Sorting Algorithms
Student Name: SWATI SINGH
Roll No: 2501730269
Section: A'''

import time
import random
import sys

# Fix for recursion error
sys.setrecursionlimit(20000)

# INSERTION SORT (O(n^2))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# MERGE SORT (O(n log n))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# QUICK SORT (Improved Version)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


def partition(arr, low, high):
    # Random pivot (important fix)
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1



# TIMING FUNCTION

def measure_time(sort_func, arr):
    temp = arr.copy()   

    start = time.time()

    if sort_func == quick_sort:
        sort_func(temp, 0, len(temp) - 1)
    else:
        sort_func(temp)

    end = time.time()

    return (end - start) * 1000



# DATASET GENERATOR

def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    random.seed(42)

    for size in sizes:
        datasets[(size, "random")] = [random.randint(1, 100000) for _ in range(size)]
        datasets[(size, "sorted")] = list(range(size))
        datasets[(size, "reverse")] = list(range(size, 0, -1))

    return datasets



# CORRECTNESS CHECK

def check_correctness():
    test = [5, 2, 9, 1, 5, 6]

    print("Correctness Check:")
    print("Original:", test)

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))

    temp = test.copy()
    print("Quick:", quick_sort(temp, 0, len(temp) - 1))



# MAIN FUNCTION

def main():
    check_correctness()

    datasets = generate_datasets()

    print("\n\n--- Performance Results (ms) ---")
    print("Size\tType\t\tInsertion\tMerge\t\tQuick")

    for (size, dtype), data in datasets.items():
        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        print(f"{size}\t{dtype}\t\t{t1:.2f}\t\t{t2:.2f}\t\t{t3:.2f}")


if __name__ == "__main__":
    main()