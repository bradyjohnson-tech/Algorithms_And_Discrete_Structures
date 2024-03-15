def insertionSort(A):
    for i in range(len(A)-2, -1, -1):
        for j in range(len(A)-1, i, -1):
            if(A[i] > A[j]):
                A.insert(j, A.pop(i))
                break
       
# O(n^2)
# T(n) = (n²-n)/2
