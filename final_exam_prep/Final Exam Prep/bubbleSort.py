def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j] > A[j + 1]:
                A[j], A[j+1] = A[j+1], A[j]

# The time complexity of Bubble Sort is O(n²), where n is the number of elements in the list A.