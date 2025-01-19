def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Example usage
print(calculator('add', 10, 5))        # Output: 15
print(calculator('subtract', 10, 5))   # Output: 5
print(calculator('multiply', 10, 5))   # Output: 50
print(calculator('divide', 10, 5))     # Output: 2.0
print(calculator('divide', 10, 0))     # Output: Error: Division by zero
print(calculator('modulus', 10, 5))    # Output: Error: Invalid operation