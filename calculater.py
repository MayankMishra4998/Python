# Calculater 
num1 = float(input("Enter the first number : "))
opperator = input("Select the Operator * + - / : ") 
num2 = float(input("Enter the second number : "))

if opperator == "+":
    print(f"The sum of {num1} and {num2} is {round(num1 + num2, 3)}")
elif opperator == "-":
    print(f"The difference of {num1} and {num2} is {round(num1 - num2, 3)}")
elif opperator == "*":
    print(f"The product of {num1} and {num2} is {round(num1 * num2, 3)}") 
elif opperator == "/":
    if num2 != 0:
        print(f"The division of {num1} and {num2} is {round(num1 / num2, 3)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"{opperator} is not a valid operator , Enter the valid operator (*, +, -, /)")    
    
    
        
    