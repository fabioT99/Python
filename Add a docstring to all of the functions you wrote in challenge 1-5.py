def squared(a):
    return a **2

def String(string):
    print(string)

String("Fabio Turco")

def misc(a, b, c, d=0, e=0):
    return(a+b*c-d+e)

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not executed")
