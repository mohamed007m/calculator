#simple calculator

#Addition function
def add(x, y):
    return x + y

#Subtraction function
def sub(x, y):
    return


#Multiplication function
def mul(x, y):
    return

#divide function
def divide(x, y):
    if y == 0:
        return "we can't divide by zero"
    return x / y

#Power function
def power(x, y):
    if y == 0:
        return 1
    return x ** y

#SquareRoot function
def sqr(x):
    return


# interface and methodology

def main():
    print("--- Simple Calculator ---\n")
    print("choose an operation:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. power")
    print("6. squareRoot")

    while True:
        choice = input("Enter your choice or press 'q' to quit: ")

        if choice.lower() == 'q':
            print("Thank you for using  our calculator. See you next time!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("enter your first number: "))
                num2 = float(input("enter your second number: "))
            except ValueError:
                print("please enter a number.")
                continue

            if choice == '1':
                print(f" ans: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f" ans: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f" ans: {num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                print(f" ans: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f" ans: {num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f" ans: root({num1}) = {sqr(num1)}")

        else:
            print("invalid input,enter valid number or press 'q' to quit.")


main()