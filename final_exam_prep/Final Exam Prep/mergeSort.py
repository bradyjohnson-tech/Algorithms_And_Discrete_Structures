def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])
        return merge(left, right)

# O(nlog(n))
