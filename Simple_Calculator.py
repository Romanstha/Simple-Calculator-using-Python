def calculator():
    print("Simple Calculator using Python")
    print("_______________________________")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus  (%)")

    while True:
        #Get user input for operation choice
        choice = input("\nEnter Operation (1-5) or 'q' to quit: ")

        #Check if user wants to quit
        if choice.lower() == 'q':
            print("Exiting Calculator...")
            break

        #Check if user input is valid
        if choice not in ['1','2','3','4','5']:
            print("Invalid Input! Please enter a number between 1 and 5 or 'q' to quit.")
            continue

        try:
            #Get user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input! Please enter a valid numeric number.")
            continue

        #Perform operation based on user choice
        if choice == '1':
            result = num1 + num2
            print(f"The addition of {num1} and {num2} is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The subtraction of {num1} and {num2} is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The multiplication of {num1} and {num2} is: {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The division of {num1} and {num2} is: {result}")
        elif choice == '5':
            if num2 == 0:
                print("Error! Modulus by zero is not allowed.")
            else:
                result = num1 % num2
                print(f"The modulus of {num1} and {num2} is: {result}")

#Call the calculator function
if __name__ == "__main__":
    calculator()
