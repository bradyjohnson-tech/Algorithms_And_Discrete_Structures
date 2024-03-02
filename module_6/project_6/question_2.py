# A)
def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)


# B)
print("===========")
print("B) The sum of squares for {} is: {}".format(12, sum_of_squares(12)))
print("B) The sum of squares for {} is: {}".format(20, sum_of_squares(20)))


# C)
# The recurrence relation that gives the work performed by the algorithm in the worst-case for a problem size of n.
#T(n) = T(n - 1) + 1
print("===========")
print("C) T(n) = T(n - 1) + 1")

# D)
# T(n) = T(n-1)+1
# T(n-1) = T[((n-1)-1]+1 = T[(n-2)+1]+1 = T(n-2)+2
# T(n-2) = T[((n-2)-1]+1 = T[(n-3)+1]+2 = T(n-3)+3
# T(n-3) = T[((n-3)-1]+1 = T[(n-4)+1]+3 = T(n-4)+4
# T(n) = T(n-k)+k
# assume n-k=0 so n=k
# so
# T(n) = T(n-n)+n
# T(n) = T(0)+n
# T(n) = 1+n
# Big-oh of n or O(n)

print("===========")
print("D)")
print("T(n) = T(n-1)+1")
print("T(n-1) = T[((n-1)-1]+1 = T[(n-2)+1]+1 = T(n-2)+2")
print("T(n-2) = T[((n-2)-1]+1 = T[(n-3)+1]+2 = T(n-3)+3")
print("T(n-3) = T[((n-3)-1]+1 = T[(n-4)+1]+3 = T(n-4)+4")
print("T(n) = T(n-k)+k")
print("assume n-k=0 so n=k")
print("so")
print("T(n) = T(n-n)+n")
print("T(n) = T(0)+n")
print("T(n) = 1+n")
print("Big-oh of n or O(n)")









