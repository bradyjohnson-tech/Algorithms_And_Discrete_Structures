n = 0

def power(x, p):
    global n
    if p < 0:
        print("Invalid power")
        return

    result = 1
    for i in range(p):
        n = n + 1
        result *= x
    return result


def evaluate(A, x):
    global n
    result = 0
    for i in range(len(A)):
        n = n + 1
        result += A[i] * power(x, i)
    return result


if __name__ == '__main__':
    A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
    print("Polynomial evaluation: {}".format(evaluate(A, 5.4)))
    print("Number of multiplications: {}".format(n))

    # from random import shuffle
    # A = list(range(70))
    # print(n)
    # print(evaluate(A, 10))
    # print("Number of multiplications: {}".format(n))
