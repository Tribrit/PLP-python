print("My calculator")

while True:
    print("Please enter a number:")
    
    x = int(input("Please enter an integer: "))
    b = int(input("Please enter a number b: "))
    
    operator = input("Please enter any operator (+, -, *, /) or 'exit' to quit: ")
    
    if operator == "+":
        print(x, "+", b, "=", (x + b), sep='')
    elif operator == "-":
        print(x, "-", b, "=", (x - b), sep='')
    elif operator == "*":
        print(x, "*", b, "=", (x * b), sep='')
    elif operator == "/":
        if b != 0:  # Check for division by zero
            print(x, "/", b, "=", (x / b), sep='')
        else:
            print("Error: Division by zero is not allowed.")
    elif operator.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid operator. Please try again.")