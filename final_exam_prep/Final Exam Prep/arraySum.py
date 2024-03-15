def arraySum(A, start, end):
    if(start == end):
        return A[start]
    else:
        mid = (start+end)//2
        return arraySum(A, start, mid) + arraySum(A, mid+1, end)

# O(n)