from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

print(logo)

first_num = int(input("What is the first number?: "))
for key in operations:
    print(key)
operation_choice = input("Pick an operation: ")
second_num = int(input("What is the second number?: "))

function = operations[operation_choice]
result = function(first_num, second_num)
print(f"{first_num} {operation_choice} {second_num} = {result}")
