def calculate(number1, number2, operation):
    """
    Perform a mathematical operation on two numbers.
    
    Args:
        number1 (int): The first number
        number2 (int): The second number
        operation (str): The operation to perform (+, -, *, /)
        
    Returns:
        int: The result of the operation
    """
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            raise ValueError("Cannot divide by zero")
        return number1 / number2
    else:
        raise ValueError("Invalid operation. Please use +, -, *, or /")

def main():
    """
    calculator program.
    """
    print("Calculator")
    print("")
    
    try:
        # Get user input
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Calculate and show result
        result = calculate(number1, number2, operation)
        print(f"{number1} {operation} {number2} = {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()