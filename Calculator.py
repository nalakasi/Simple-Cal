# Simple calculator function
def calculator():
    # Display available operations
    print("Simple Calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Ask user to select an operation
    choice = input("Select operation (1/2/3/4): ")

    # Input validation for operation choice
    if choice in ['1', '2', '3', '4']:
        # Input two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the operation based on the user's choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            # Handle division by zero
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input, please enter a valid option (1/2/3/4)")

# Call the calculator function
calculator()

