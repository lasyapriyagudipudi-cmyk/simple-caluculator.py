import math

print("Welcome to the simple calculator!")

num1 = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /)): ")
num2 = int(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2            
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"
    print("Wrong operation! Please enter a valid operation (+, -, *, /).")

print(num1, operation, num2, "=", result)
