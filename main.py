def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

should_continue = True

num1 = int(input("What's the first number?:"))

while should_continue:
    for keys in operations:
        print(keys)

    operation_symbol = input("Pick an operation from the lines above: ")
    num2 = int(input(f"{num1} {operation_symbol} What's the second number?:"))
 
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    

    should_continue = input('Should we continue with the calculation? Type "no" to stop. ').lower()
    if should_continue == "no":
        should_continue = False
    else:
        should_continue = True
    num1 = answer

    