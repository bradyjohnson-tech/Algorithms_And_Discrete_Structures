def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = lomuto_partition(arr, low, high)
    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)


def kth_smallest(arr, k):
    if k < 0 or k >= len(arr):
        return None
    return quickselect(arr, 0, len(arr) - 1, k)