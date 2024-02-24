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
calculator_continue = 'y'

print(logo)

first_num = int(input("What is the first number?: "))
for key in operations:
    print(key)
while calculator_continue == 'y':
    operation_choice = input("Pick an operation: ")
    second_num = int(input("What is the next number?: "))
    function = operations[operation_choice]
    result = function(first_num, second_num)
    print(f"{first_num} {operation_choice} {second_num} = {result}")
    calculator_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.:")
    if calculator_continue == 'y':
        first_num = result
