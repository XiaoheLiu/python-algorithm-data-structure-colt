# Helper functions for sorting algorithms


def min_index(arr: list, i: int) -> int:
    """
    Return the index of the minimum element among the elements from i to the end in arr.
    Helper function for selection sort.
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
    Helper function for merge sort.
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


def pivot(arr: list, start: int, end: int) -> int:
    """
    Set start element as pivot, then move the smaller elements to the left, larger elements to the right.
    Returns the final position of the pivot after the array has been pivoted.
    Helper function for quick sort.
    """

    # Set pivot as the first element
    pivot = arr[start]
    swap_idx = start

    # Loop from the second element until the end:
    for i in range(start+1, end+1):
        # If the current element is smaller than the pivot:
        if arr[i] < pivot:
            swap_idx += 1  # increment swap_idx
            # pivot the small element to the left
            arr[swap_idx], arr[i] = arr[i], arr[swap_idx]

    # Finally, put the pivot the the correct position
    arr[start], arr[swap_idx] = arr[swap_idx], arr[start]

    # Returns the position of the pivot
    return swap_idx
