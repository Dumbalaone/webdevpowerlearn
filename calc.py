num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
op2=input("enter an operator")
if op2 == "+":
    result = num1+num2
    print(result)
elif op2 == "-":
    result = num1-num2
    print(result)
elif op2 == "*":
     result = num1 * num2
     print(result)
elif op2 == "/":
    result =num1/num2
    print(result)
else:
    print("invalid operator")