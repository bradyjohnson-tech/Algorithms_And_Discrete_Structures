import math


# A)
def binary_digits_count(n):
    # Base case: when n is 1, so we return 1
    if n == 1:
        return 1
    # Recursive case: when n > 1, the answer is 1 more than the number of digits
    # in the binary representation of n/2
    else:
        return 1 + binary_digits_count(math.floor(n / 2))


if __name__ == '__main__':
    # B)
    # 256 => 100000000
    print("===========")
    print("B) Number of digits in the binary representation of {}: {}".format(256, binary_digits_count(256)))
    # 750 => 1011101110
    print("B) Number of digits in the binary representation of {}: {}".format(750, binary_digits_count(750)))

    # C)
    # The recurrence relation that gives the work performed by the algorithm in the worst-case for a problem size of n.
    # T(n) = T(n/2) + 1
    print("===========")
    print("C) T(n) = T(n/2) + 1")

    # D)
    # This algorithms time complexity and asymptotic behavior is Big-oh log(n)
    # a = 1
    # b = 2
    # f(n) = 1
    # log_b(a) = log_2(1) = 0
    # f(n) = 1 > log_2(1), So we have case 2
    # T(n) = Θ(n^log_b(a) * log n) = Θ(log n)
    print("===========")
    print("D)")
    print("a = 1")
    print("b = 2")
    print("f(n) = 1")
    print("log_b(a) = log_2(1) = 0")
    print("f(n) = 1 > log_2(1), So we have case 2")
    print("T(n) = Θ(n^log_b(a) * log n) = Θ(log n)")
    print("Big-oh of Θ(log n)")
