a = input("Insert a value: ")
b = input("Insert another value: ")
a = int(a)
b = int(b)
try:
    c = a / b
    print("The result is: %.f" %c)
except 	ZeroDivisionError:
    print("You cannot divide by 0")