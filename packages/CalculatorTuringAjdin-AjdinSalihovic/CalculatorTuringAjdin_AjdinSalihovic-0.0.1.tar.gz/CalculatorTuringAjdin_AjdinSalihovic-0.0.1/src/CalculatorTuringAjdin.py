#Creation of the Python calculator for Turing college
#Signature: Ajdin Salihovic

# This function is for adding two numbers
def add(x, y):
    return x + y

# This function is for subtracting two numbers
def subtract(x, y):
    return x - y

# This function is for multiplying two numbers
def multiply(x, y):
    return x * y

# This function is for dividing two numbers
def divide(x, y):
    return x / y

# This takes (n) root of a number.
def nRoot(x, y):
    return x ** (1/y)


print("Select operation.")
print("1.Add +")
print("2.Subtract -")
print("3.Multiply *")
print("4.Divide /")
print("5. Takes (n) root of a number **")

while True:
    # This takes the input from the user
    choice = input("Please choose (1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**(1/", num2, ")", "=", nRoot(num1, num2))


        # check if user wants another calculation
        # break the while loop if answer is no

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")