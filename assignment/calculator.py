# Calculator

num1 = int(input(" Input the first number >>> "))
num2 = int(input(" Input the second number >>> "))
sign = input(" Input symbol of operation from +, -, *, / >>> ")

if sign == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif sign == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif sign == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif sign == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide number by 0")
elif sign != "+" and sign != "-" and sign != "*" and sign != "/":
    print("invalid operator: Please choose from ")
else:
    print("Invalid Combination Sequence")