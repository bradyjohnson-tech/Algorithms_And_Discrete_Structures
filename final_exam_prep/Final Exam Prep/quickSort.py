def lomuto(A, left, right):
    p = A[left]
    i = left
    for j in range(left, right):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

def quickSort(A, left, right):
    if left < right:
        mid = lomuto(A, left, right)
        quickSort(A, left, mid-1)
        quickSort(A, mid+1, right)


# Test the function
A = [127, 48, 62, 51, 198, 17, 52, 209]
quickSort(A, 0, len(A) - 1)
print(A)  # prints: [17, 48, 51, 52, 62, 127, 198, 209]
# O(n^2)
# average O(nlog(n))