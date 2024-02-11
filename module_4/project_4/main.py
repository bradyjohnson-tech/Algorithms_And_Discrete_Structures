def divisible_by(nums: [int], n: int):
    count = 0
    if n <= 0:
        raise ValueError(
            "N should be a positive integer.")  # print statement instead of throwing error unless i wrap the call in a
        # try catch.
    else:
        for num in nums:
            if num % n == 0:  # if the remainder is equal to zero, then the value at the index is evenly divisible.
                count += 1
        return count  # return the number of values divisible by n.


def smallest_gap(nums: [int]):
    min_gap = float('inf')
    for i in range(len(nums) - 1):  # iterate through the array in order.
        gap = abs(nums[i + 1] - nums[i])  # calculate the number of units between the numbers
        if gap < min_gap:  # check if the gap is smaller than the smallest gap already found.
            min_gap = gap
    return min_gap


def matrix_multiplication(nxn: int, matrix_a, matrix_b):
    if nxn < 2:
        raise ValueError("nxn variable cannot be less than 2.")

    # Initialize the product matrix with 0s
    product = [[0 for _ in range(nxn)] for _ in range(nxn)]

    # Compute the product of (matrix_a * matrix_b)
    for i in range(nxn):
        for j in range(nxn):
            for k in range(nxn):
                product[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return product


if __name__ == '__main__':
    print("---- Question 1 ----")
    print("a): " + str(divisible_by([20, 21, 25, 28, 33, 34, 35, 36, 41, 42], 7)))
    print("b): " + str(divisible_by([18, 54, 76, 81, 36, 48, 99], 9)))

    print("---- Question 2 ----")
    print("a): " + str(smallest_gap([50, 120, 250, 100, 20, 300, 200])))
    print("b): " + str(smallest_gap([12.4, 45.9, 8.1, 79.8, -13.64, 5.09])))

    print("---- Question 3 ----")
    n = 2
    A = [[2, 7], [3, 5]]
    B = [[8, -4], [6, 6]]
    print("a): " + str(matrix_multiplication(n, A, B)))
    n = 3
    A = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
    B = [[.3, .25, .1], [.44, .8, .1], [-.5, .75, .6]]
    print("b): " + str(matrix_multiplication(n, A, B)))
