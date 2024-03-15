def array_diff_brute_force(A, B):
    C = []
    for element_A in A:
        match_found = False
        for element_B in B:
            if element_A == element_B:
                match_found = True
                break
        if not match_found:
            C.append(element_A)
    return C

A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
B = [35, 45, 55, 60, 50, 40]
print(array_diff_brute_force(A, B))