import CustomQueue
import CustomStack


def QueStack():
    queue = CustomQueue.CustomQueue()
    stack = CustomStack.CustomStack()

    while True:
        input_value = input("Enter a positive number: ")
        result = read_user_input(input_value)
        if result is None:
            break
        queue.enqueue(result)
        stack.push(result)

    if stack.size() >= 2 or queue.size() >= 2:
        for i in range(2):
            stack.pop()
            queue.dequeue()

    print("\n-- Stack --")
    print(stack.print_contents())

    print("\n-- Queue --")
    print(queue.print_contents())


def read_user_input(input_value):
    try:
        user_input = float(input_value)
        if user_input > 0:
            return user_input
        else:
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


QueStack()
