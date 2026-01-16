print('Python is running in vsCode')

name = input("Enter your name")
print("Hello", name)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

op = input("Choose operation (+, -, *, /): ")

if op == "+" : 
    print("Result: ", num1 + num2)
elif op == "-":
    print("Result: ", num1 - num2)
elif op == "*": 
    print("Result: ", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1/ num2)
    else: print("Error: cannot divide by zero")

else: 
    print("Invalid operation")