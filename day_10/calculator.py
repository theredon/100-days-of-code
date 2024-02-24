from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    calculator_continue = True
    first_num = int(input("What is the first number?: "))
    for key in operations:
        print(key)
    while calculator_continue:
        operation_choice = input("Pick an operation: ")
        second_num = int(input("What is the next number?: "))
        function = operations[operation_choice]
        result = function(first_num, second_num)
        print(f"{first_num} {operation_choice} {second_num} = {result}")
        program_continue = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'end' to end.: ")
        if program_continue == 'y':
            first_num = result
        elif program_continue == 'n': 
            calculator_continue = False
            calculator()
        else:
            calculator_continue = False


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

print(logo)

calculator()