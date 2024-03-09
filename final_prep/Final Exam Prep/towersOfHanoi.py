def hanoi(n):
    if (n == 0):
        return 0
    else:
        return 2 * hanoi(n - 1) + 1


for i in range(10):
    print("with {} disks you need {} movement".format(i, hanoi(i)))

# O(2^n),