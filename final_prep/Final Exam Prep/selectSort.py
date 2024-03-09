def selectSort(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if(A[j] < A[minIndex]):
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]

 # The time complexity of the Selection Sort algorithm is O(n²), where n is the number of elements in the list A.
