def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Division by zero not possible.")
        return 0
    else:
        return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print("Logos maximos")
    a = float(input("What's the first number?"))
    while True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        if operation not in operations:
            print("Wrong symbol.")
            break
        b = float(input("What's the next number?: "))

        function = operations[operation]
        result = function(a, b)

        print(f"{a} {operation} {b} = {result}")

        if input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ") == 'n':
            # Recursion
            calculator()
        else:
            a = result


calculator()
