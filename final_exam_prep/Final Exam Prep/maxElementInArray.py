def Maximum(A, right):
    if right == 0:
        return A[0]
    else:
        max_of_other_elements = Maximum(A, right-1)
        if A[right] > max_of_other_elements:
            return A[right]
        else:
            return max_of_other_elements


A = [17, 62, 49, 73, 26, 51]
print(Maximum(A, len(A)-1))

#print("the maximum number is", A[i], "at index", i)


# In the function, the list is divided into two halves with each recursive call until we reach arrays of single elements. This breakdown is done log(n) times for a list of n elements. We can thus say that the function exhibits log(n) divisions.
# After reaching the smallest possible subarray (1 element), each subarray is built up back again to form the original list. This is done in n operations since we have n elements.
# So, overall the time complexity of this function is n times log(n) operations. Thus, we say that the time complexity of this method is O(nlogn).

# recursive
#O(n)

# Divide and conquor
# O(nlogn)