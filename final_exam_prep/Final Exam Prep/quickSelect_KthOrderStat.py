from typing import List


# KthOrderStatistic
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

# O(n^2)
# average = (n)