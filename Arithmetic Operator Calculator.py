a = float(input("Insert an addend value: "))
b = float(input("Insert another addend value: "))
c = a + b
print("The result of the sum is: %.2f \n" %c)

a = float(input("Insert a subtraction value: "))
b = float(input("Insert another subtraction value: "))
c = a - b
print("The result of the subtraction is: %.2f \n" %c)

a = float(input("Insert a multiplication value: "))
b = float(input("Insert another multiplication value: "))
c = a * b
print("The result of the multiplication is: %.2f \n" %c)

a = float(input("Insert a dividend value: "))
b = float(input("Insert a divisor value: "))
try:
    c = a / b
    print("The result of the division is: %.2f \n" %c)
except 	ZeroDivisionError:
    print("You cannot divide by 0")

a = int(input("Insert a number: "))
b = int(input("Insert an exponent: "))
c = a ** b
print("The result of the power is: %.f" %c)