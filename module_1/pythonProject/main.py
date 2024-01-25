import utils
from linked_list import LinkedList

L = LinkedList()


def read_vector_from_file(filename='data.txt'):
    # Read numbers from a file into a vector of integers
    with open(filename, 'r') as file:
        a = [int(line.strip()) for line in file]
    a.sort()
    return a


def vector_to_linked_list(a):
    for _ in a:
        L.insert_at_end(_)


def user_input():
    return int(input(f"Please enter an integer value: ".strip()))


def main():
    a = read_vector_from_file("data.txt")
    vector_to_linked_list(a)
    x = user_input()
    L.insert_in_order(x)
    L.print()


main()

# utils.generate_non_repeating_vector_and_save(16)
