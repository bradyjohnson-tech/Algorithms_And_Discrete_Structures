import random


def generate_non_repeating_vector_and_save(size, filename='data.txt'):
    # Check if the size is greater than 1
    if size <= 1:
        raise ValueError("Vector size must be greater than 1 for non-repeating numbers.")

    # Generate a vector of non-repeating numbers using random.sample
    my_vector = random.sample(range(1, 1000 + 1), size)

    # Save the vector to a file, each number on a new line
    with open(filename, 'w') as file:
        for number in my_vector:
            file.write(str(number) + '\n')

    return my_vector

