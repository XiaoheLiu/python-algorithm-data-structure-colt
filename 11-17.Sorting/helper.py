# Helper functions for sorting algorithms


def min_index(arr: list, i: int) -> int:
    """
    Return the index of the minimum element among the elements from i to the end in arr
    """
    ind = i
    min_num = arr[i]
    for j in range(i, len(arr)):
        if arr[j] < min_num:
            ind = j
            min_num = arr[j]

    return ind


def merge(arr1: list, arr2: list) -> list:
    """
    Merge two sorted arrays into one sorted array.
    """
    arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    # Collect the rest of the elements into arr, if any
    arr.extend(arr1[i:])
    arr.extend(arr2[j:])

    return arr
