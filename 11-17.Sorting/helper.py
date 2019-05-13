# Helper functions for sorting algorithms


def min_index(arr, i):
    """
    Return the index of the minimum element from i to the end in arr
    """
    ind = i
    min_num = arr[i]
    for j in range(i, len(arr)):
        if arr[j] < min_num:
            ind = j
            min_num = arr[j]

    return ind
