def lomuto(A, left, right):
    p = A[left]
    i = left
    for j in range(left, right):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i

A = [100, 213, 65, 29, 153, 199, 47,181,85]
pvt = lomuto(A, 0, len(A)-1)
print("Lomuto with pivot at", pvt, ":", A[pvt])
print(A[:pvt])
print(A[:pvt+1])

# big-oh of: O(n * log(n))