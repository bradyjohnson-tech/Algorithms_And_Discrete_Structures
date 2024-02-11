import csv

from Person import Person
from Stack import Stack

people = []
stack = Stack()


def read_people_csv(filename='people.csv'):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            people.append(Person(row[1], row[2], row[0], row[3]))


def read_user_input():
    try:
        user_input = int(input("Enter 1,2,3 or 4:"))
        if 5 > user_input > 0:
            return user_input
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


read_people_csv()

# Add a list of people to the stack
for person in people:
    stack.push(person)

# interface with the user to see how many people to take off the stack.
while True:
    result = read_user_input()
    if result is None:
        continue
    for i in range(result):
        stack.pop()
    if stack.is_empty():
        quit()
    if type(stack.peek()) is Person:
        print(stack.peek().name)

