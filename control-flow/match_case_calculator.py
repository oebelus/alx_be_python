one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {one + two}")
    case "-":
        print(f"The result is {one - two}")
    case "*":
        print(f"The result is {one * two}")
    case "/":
        if two == 0:
            print("Division by zero is not allowed.")