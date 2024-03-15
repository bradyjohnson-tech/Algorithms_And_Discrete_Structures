def recursiveFibonacci(n):
    if (n in [1,2]):
        return 1
    else:
        return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))

 # In terms of Big O notation, the time complexity of this recursive Fibonacci function is exponential, often denoted as O(2^n)



def fibonacci(n):
    if (n in [1,2]):
        return 1
    else:
        nMinus2 = 1
        nMinus1 = 1
        for i in range(3, n+1):
            nMinus2, nMinus1 = nMinus1, nMinus2 +nMinus1
    return nMinus1

print(fibonacci(10))

# Therefore, the overall complexity is O(n).
# f(n) = F(n-1) + F(n-2) if n>2