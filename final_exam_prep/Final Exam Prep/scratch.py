


def uniqueElements(A):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)-1):
            if A[i] == A[j]:
                return False
    return True
# The function uniqueElements(A) uses nested loops, which typically suggest a quadratic time complexity, O(n²), where n is the length of the list A



def binaryDigitCount(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2

# The provided code is a classic example of a loop that halves the input n at each iteration until n becomes less than or equal to 1.
# In terms of time complexity or T(n), this is characterized as O(log n), specifically O(log n) to the base 2, because we are continuously dividing n by 2 in each iteration.
# In this case, log n refers to the number of steps/iterations required to reduce n to 1 using division by 2.
# In summary, the time complexity T(n) of the given code is O(log n) to the base 2.