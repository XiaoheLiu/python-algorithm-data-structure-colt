from helper import min_index, merge, pivot


def bubble_sort(arr):
    length = len(arr)
    # 1. Loop over start to end
    for i in range(length):
        no_swaps = True
        # 2. Check every adjacent elements
        for j in range(length-1):
            # if in decending order, swap:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                no_swaps = False
        # Stop looping is no swap has happened
        if no_swaps:
            break
    return arr


def selection_sort(arr):
    # 1. Loop over entire array
    for i in range(len(arr)):
        # Find the index of the minimum element from i to the end
        ind = min_index(arr, i)
        # Swap the 1st element with the minimum element
        arr[ind], arr[i] = arr[i], arr[ind]

    return arr


def insertion_sort(arr):
    # 1. Loop from the first element (if empty array, returns empty array directly)
    for i in range(1, len(arr)):
        # 2. Save the current element
        current = arr[i]
        # 3. Take the portion of array on the current element's left,
        # and loop the portion in descending order
        j = i-1
        while j >= 0 and arr[j] > current:
            # Shift the elements that are larger than the current to the right
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = current  # put current value in the empty slot
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr)//2

    # Merge sort the left and right halves recursively
    left = merge_sort(arr[:middle_index])
    right = merge_sort(arr[middle_index:])

    return merge(left, right)


def quick_sort(arr):
    quick_sort_wrapper(arr, left=0, right=len(arr)-1)
    return arr


def quick_sort_wrapper(arr, left, right):
    """
    Sort the partition of the array from left to right.
    """
    if left < right:
        pivot_idx = pivot(arr, left, right)
        quick_sort_wrapper(arr, left, pivot_idx-1)
        quick_sort_wrapper(arr, pivot_idx+1, right)
