def recursivehanoi(n):
    if (n == 0):
        return 0
    else:
        return 2 * recursivehanoi(n - 1) + 1


for i in range(10):
    print("with {} disks you need {} movement".format(i, recursivehanoi(i)))

# O(2^n),


def hanoi(n):
    ans = 0
    for i in range(n):
        ans = 2 * ans + 1
    return ans

for i in range(10):
    print("with {} disks you need {} movement".format(i, hanoi(i)))

# O(n)
# T(n) = 2 T(n-1) + 1

# The time complexity O(n) is more efficient than O(2^n).
