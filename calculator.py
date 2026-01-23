# Simple calculator

# Addition function
def add(x, y):
    return x + y


# Subtraction function
def sub(x, y):
    return x - y


# Multiplication function
def mul(x, y):
    return x * y


# Divide function
def divide(x, y):
    if y == 0:
        return "we can't divide by zero"
    return x / y


# Power function
def power(x, y):
    if y == 0:
        return 1
    return x ** y


# Root function
def root(x, n):
    if n == 0:
        return "root degree can't be zero"
    if x < 0 and n % 2 == 0:
        return "can't take even root of negative number"
    return x ** (1 / n)


# interface and methodology

def main():
    print("--- Simple Calculator ---\n")
    print("choose an operation:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. power")
    print("6. root")

    while True:
        choice = input("Enter your choice or press 'q' to quit: ")

        if choice.lower() == 'q':
            print("Thank you for using our calculator. See you next time!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("enter your first number: "))
                num2 = float(input("enter your second number: "))
            except ValueError:
                print("please enter a number.")
                continue

            if choice == '1':
                print(f"ans: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"ans: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"ans: {num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                print(f"ans: {num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            try:
                base = float(input("enter the base: "))
                exponent = float(input("enter the exponent: "))
            except ValueError:
                print("please enter a number.")
                continue

            print(f"ans: {base} ^ {exponent} = {power(base, exponent)}")

        elif choice == '6':
            try:
                num = float(input("enter the number: "))
                degree = float(input("enter the root degree: "))
            except ValueError:
                print("please enter a number.")
                continue

            print(f"ans: root({num}, {degree}) = {root(num, degree)}")

        else:
            print("invalid input, enter valid number or press 'q' to quit.")


# Run the main function (The program)
main()
