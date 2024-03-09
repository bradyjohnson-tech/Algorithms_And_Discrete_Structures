def stringMatching(S, R):
    for i in range(len(S)-len(R)+1):
        j, k = i, 0
        while k < len(R) and S[j] == R[k]:
                j += 1
                k += 1
            if k == len(R):
                return i
        return None

# Therefore, the total number of character comparisons in worst case can be up to n * m, hence the time complexity of the algorithm is O(nm).