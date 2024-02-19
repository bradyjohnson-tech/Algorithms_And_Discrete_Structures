def bubble_sort(a):
    iteration = 0
    total_comparisons = 0
    total_swaps = 0
    for i in range(len(a) - 1):
        iteration = iteration + 1
        compared = 0
        swapped = 0
        for j in range(len(a) - i - 1):
            compared = compared + 1
            if a[j] > a[j + 1]:
                swapped = swapped + 1
                a[j], a[j + 1] = a[j + 1], a[j]

        total_swaps += swapped
        total_comparisons += compared

        if swapped == 0:
            print("---------------------------")
            print("===========================")
            print("---------------------------")
            print("Returned early on Iteration Kth = {iteration}".format(iteration=iteration))
            print("Array: {}".format(a))
            print("Total comparisons: {}".format(total_comparisons))
            print("Total swaps: {}".format(total_swaps))
            exit()

        print("===========================")
        print("Iteration Kth = {iteration}".format(iteration=iteration))
        print(a)
        print("Comparisons: {}".format(compared))
        print("Swaps:{}".format(swapped))


if __name__ == '__main__':
    A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

    bubble_sort(A4)
