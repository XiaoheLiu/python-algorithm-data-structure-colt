from helper import min_index


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
