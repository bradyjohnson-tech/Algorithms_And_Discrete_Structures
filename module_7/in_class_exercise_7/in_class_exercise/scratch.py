def LomutoPartition(A, lo, hi):
    pivot = A[lo]
    s = lo
    for i in range(lo+1, hi+1):
        if A[i] < pivot:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[lo], A[s] = A[s], A[lo]
    return A


A = [100, 213, 65, 29, 153, 199, 47, 181, 85]
print(LomutoPartition(A, 0, len(A) - 1))