def binSearch(A, start, end, k):
    mid = (end+start)//2
    if (start > end):
        return None
    elif (A[mid] == k):
        return mid
    elif (A[mid] > k):
        return binSearch(A, start, mid-1, k)
    else:
        return binSearch(A, mid+1, end, k)


# So, the time complexity of binSearch(A, start, end, k) function is O(log n).

# The data must be pre-sorted