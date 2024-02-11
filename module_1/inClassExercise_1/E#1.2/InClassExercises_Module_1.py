def vecSwap():
    user_input = int(input(f"Enter and even integer between 9 and 21".strip()))

    if 9 > user_input < 21:
        raise ValueError("Vector length must an integer between 9 and 21.")

    if user_input % 2 != 0:
        raise ValueError("Vector length must be even for swapping pairs.")

    # Create array
    vector = list(range(0, user_input))

    # Loop to swap pairs
    for i in range(0, len(vector), 2):
        vector[i], vector[i + 1] = vector[i + 1], vector[i]

    print(vector)


def zigzag(a, b, c):
    if a < b > c:
        return True
    elif a > b < c:
        return True
    else:
        return False
