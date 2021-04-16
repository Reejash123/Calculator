# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("0. Add")
print("1. Subtract")
print("2. Multiply")
print("3. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(0/1/2/3): ")

    # Check if choice is one of the four options
    if choice in ('0', '1', '2', '3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input('Enter second number: '))

        if choice == '0': 
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '1':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '2':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '3':
            print(num1, '/', num2, '=', divide(num1, num2))
        break
    else:
        print("Number is not valid")

