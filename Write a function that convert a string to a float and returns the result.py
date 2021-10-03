def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not executed")
c = convert(3.7)
print(c)
    
