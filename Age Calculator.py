name1 = "Luke"
current_year1 = 2021
DOB1 = 2018

name2 = "Mark"
current_year2 = 2021
DOB2 = 2005

name3 = "John"
current_year3 = 2021
DOB3 = 1950

def age_calculator(name, current_year, DOB):
    age = current_year - DOB
    print("age: ")
    print(age)
    if age < 18:
        return name + " is not an adult"
    else:
        return name + " is an adult"
result1 = age_calculator(name1, current_year1, DOB1)
result2 = age_calculator(name2, current_year2, DOB2)
result3 = age_calculator(name3, current_year3, DOB3)
print(result1)
print(result2)
print(result3)