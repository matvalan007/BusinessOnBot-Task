import operator

# define available operations
operations = {
    'addition': operator.add,
    'subtraction': operator.sub,
    'multiplication': operator.mul,
    'division': operator.truediv,
    'add': operator.add,
    'subtract': operator.sub,
    'multiply': operator.mul,
    'divide': operator.truediv,
    'remainder': operator.mod,
    'power': operator.pow
}

# define function to get user input
def get_input():
    print("BOT : What mathematical operation do you want to do?")
    operation = input("USER: ")
    operation = operation.lower()
    print("BOT : Enter the first operand")
    operand1 = float(input("USER: "))
    print("BOT : Enter the second operand")
    operand2 = float(input("USER: "))
    return (operation, operand1, operand2)

# define main function
def main():
    print("BOT : Hi..! I am math bot...I do mathematical operations like : \n\t1. Addition\n\t2. Subtraction\n\t3. Multiplicaton\n\t4. Division\n\t5. Remainder\n\t6. Power")
    input("USER: ")
    while True:
        operation, operand1, operand2 = get_input()
        if operation in operations:
            if (operation == 'division'or operation == 'divide') and operand2 == 0.0:
                print("BOT : Invalid Input....")
            else:
                result = operations[operation](operand1, operand2)
                print(f"BOT : {operation} of {operand1} and {operand2} is {result}")
        else:
            print("BOT : Invalid operation....")
        
        print("BOT : Do you want to do more operations? (yes/no) ")
        more_operations = input("USER: ")
        if more_operations.lower() != "yes":
            break

if __name__ == '__main__':
    main()
