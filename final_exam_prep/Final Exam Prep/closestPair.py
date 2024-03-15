def closestPair(P):
    minDist, ans = float("inf"), []
    for i in range(len(P)-1):
        for j in range(i+1, len(P)):
            dist = 0
            for k in range(len(P[i])):
                dist += (P[i][k] - P[j][k])**2
            dist = dist ** 0.5
            if dist < minDist:
                minDist, pair = dist, [i,j]
    return pair[0], pair[1]

# The time complexity is O(n^2 * d), where n is the number of points in the list P and d is the dimension of the points.
# Here's why:
# The outer loop runs n times.
# Within the outer loop, a nested loop runs n - i times where i is the current iteration of the outer loop. Together, the outer and inner loop amount to O(n^2) operations.
# Within the nested loop, there is a third loop calculating the Euclidean distance, which runs d times, where d is the dimension of the points (len(P[i])). This results in O(d) operations.
# Since these loops are nested, you multiply the numbers of operations together, thus the time complexity is O(n^2 * d)

