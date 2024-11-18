
# get numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# convert to strings to numbers
num1 = float(num1)
num2 = float(num2)

# ask for the operation
operation = input("Enter the operations (+, -, *, /): ")

# perform calculations
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid Operation"

print(result)