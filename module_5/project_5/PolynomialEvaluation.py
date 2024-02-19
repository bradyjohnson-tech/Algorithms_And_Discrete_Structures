def power(x, p):
    if p < 0:
        print("Invalid power")
        return

    result = 1
    for i in range(p):
        result *= x
    return result


def evaluate(A, x):
    result = 0
    for i in range(len(A)):
        result += A[i] * power(x, i)
    return result


if __name__ == '__main__':