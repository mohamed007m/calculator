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
          print("we can't divide by zero")
          return None 
    return x / y


# Power function
def power(x, y):
    if y == 0:
        return 1
    return x ** y


# Root function
def root(x, n):
    if n == 0:
         print("root degree can't be zero")
         return None
    if x < 0 and n % 2 == 0:
         print("can't take even root of negative number")
         return None
    return x ** (1 / n)


# interface and methodology

def main():
    ans = None
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
              if ans is not None:
                  use_ans = input("Do you want to use previous answer? (y/n): ")
                  if use_ans.lower()=='y':
                      num1 = ans
                  else :
                      num1=float(input("enter your first number: "))
              else:
                  num1=float(input("enter your first number: "))

              num2 = float(input("enter your second number: "))
              
            except ValueError:
                print("please enter a number.")
                continue

            if choice == '1':
                ans = add(num1, num2)
                print(f"ans: {num1} + {num2} = {ans}")
            elif choice == '2':
                ans = sub(num1, num2)
                print(f"ans: {num1} - {num2} = {ans}")
            elif choice == '3':
                ans = mul(num1, num2)
                print(f"ans: {num1} * {num2} = {ans}")
            elif choice == '4':
                result = divide(num1, num2)
                if result is None:
                   continue
                ans = result
                print(f"ans: {num1} / {num2} = {ans}")

        elif choice == '5':
            try:
                if ans is not None:
                  use_ans = input("Do you want to use previous answer? (y/n): ")
                  if use_ans.lower()=='y':
                      base = ans
                  else :
                      base=float(input("enter your base number: "))
                else:
                   base=float(input("enter your base number: "))

                exponent = float(input("enter the exponent: "))

            except ValueError:
                print("please enter a number.")
                continue
            ans = power(base, exponent)
            print(f"ans: {base} ^ {exponent} = {ans}")

        elif choice == '6':
            try:
                if ans is not None:
                  use_ans = input("Do you want to use previous answer? (y/n): ")
                  if use_ans.lower()=='y':
                      num = ans
                  else :
                      num = float(input("enter the number: "))
                else:
                      num = float(input("enter the number: "))

                degree = int(input("enter the root degree: "))
                
                
            except ValueError:
                print("please enter a number.")
                continue

            result = root(num, degree)
            if result is None:
                 continue
            ans = result
            print(f"ans: root({num}, {degree}) = {ans}")

        else:
            print("invalid input, enter valid number or press 'q' to quit.")


# Run the main function (The program)
main()
