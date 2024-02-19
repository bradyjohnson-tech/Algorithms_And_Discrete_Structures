def stringMatching(S, R):
    for i in range(len(S)-len(R)+1):
        j, k = i, 0
        while (k < len(R)) and (S[j] == R[k]):
            j += 1
            k += 1
        if( k == len(R)):
            return i
    return None

s = "ALGORITHM"
r = "RIT"

print(stringMatching(s, r))
