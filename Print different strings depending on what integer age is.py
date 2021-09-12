CurrentYear = 2021
MarkDOB = 2019
ThomasDOB = 2011
FabioDOB = 2003
JohnDOB = 1950

firstAge = CurrentYear - MarkDOB
secondAge = CurrentYear - ThomasDOB
thirdAge = CurrentYear - FabioDOB
fourthAge = CurrentYear - JohnDOB

if firstAge < 5:
    print ("Mark is a kid")
elif firstAge < 10:
    print("Mark is a boy")
elif firstAge == 18:
    print("Mark is an adult")
else:
    print("Mark is old")

if secondAge < 5:
    print ("Thomas is a kid")
elif secondAge >= 10:
    print("Thomas is a boy")
elif secondAge == 18:
    print("Thomas is an adult")
else:
    print("Thomas is old")

if thirdAge < 5:
    print ("Fabio is a kid")
elif thirdAge < 10:
    print("Fabio is a boy")
elif thirdAge == 18:
    print("Fabio is an adult")
else:
    print("Fabio is old")

if fourthAge < 5:
    print ("John is a kid")
elif fourthAge < 10:
    print("John is a boy")
elif fourthAge == 18:
    print("John is an adult")
else:
    print("John is old")