name1 = "Fabio"
months1 = 12
salary_per_year1 = 1500

name2 = "Sandra"
months2 = 12
salary_per_year2 = 800

name3 = "Jodie"
months3 = 12
salary_per_year3 = 1000

def tax_calculator(name, months_per_12, salary_per_year):
    tax = salary_per_year * months_per_12
    if tax >= 12000:
        return name + " needs to pay taxes"
    else:
        return name + " doesn't need to pay taxes"
result1 = tax_calculator(name1, salary_per_year1, months1)
result2 = tax_calculator(name2, salary_per_year2, months2)
result3 = tax_calculator(name3, salary_per_year3, months3)
print(result1)
print(result2)
print(result3)