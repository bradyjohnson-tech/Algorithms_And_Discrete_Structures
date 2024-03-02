import random
from typing import List


def generate_random_array(length):
    return [random.randint(0, 10000) for _ in range(length)]


def QuickSelect(array: List[int], k: int):
    k -= 1

    def quick_select(l, r):
        pivot, p = array[r], l
        for i in range(l, r):
            if array[i] <= pivot:
                array[p], array[i] = array[i], array[p]
                p += 1
        array[p], array[r] = array[r], array[p]

        if p > k:
            return quick_select(l, p - 1)
        if p < k:
            return quick_select(p + 1, r)
        else:
            return array[p]

    return quick_select(0, len(array) - 1)


if __name__ == '__main__':
    k_input = input("Please enter the value of k you would like to find: ")
    generated_array = generate_random_array(1000)
    smallest = QuickSelect(generated_array, int(k_input))
    print("The {0}th smallest element in the array is {1}".format(k_input, smallest))
