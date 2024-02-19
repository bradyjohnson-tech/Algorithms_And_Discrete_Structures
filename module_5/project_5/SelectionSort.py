def selection_sort(a):
    iteration = 0
    for i in reversed(range(len(a))):
        maxIndex = i
        iteration = iteration + 1
        compared = 0
        swapped = 0
        for j in range(i):
            compared = compared + 1
            if a[j] > a[maxIndex]:
                maxIndex = j
        swapped = swapped + 1
        a[i], a[maxIndex] = a[maxIndex], a[i]
        print("Iteration Kth = {iteration}".format(iteration=iteration))
        print(a)
        print(compared)
        print(swapped)

    return a


if __name__ == '__main__':
    A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
    A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
    print(selection_sort(A1))
    print(selection_sort(A2))
    print(selection_sort(A3))
