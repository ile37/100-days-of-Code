from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    number1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    
    while True:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        new_calculation = operations[operation_symbol](number1, next_number)

        print(f"{number1} {operation_symbol} {next_number} = {new_calculation}")

        cmd = input(f"Type 'q' to Quit, 'y' to continue calculation with {new_calculation}, or Type 'n' to to start a new calcutaion: ")
        if cmd == "n":
            calculator()
        elif cmd == "q":
            break

        number1 = new_calculation

print(logo)
calculator()