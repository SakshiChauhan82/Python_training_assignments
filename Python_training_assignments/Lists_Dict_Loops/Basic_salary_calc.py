employee = []
num = int(input("enter n. of employees"))
for i in range(num):
    print("Enter details of the employee")
    name = input("enter employee name")
    basic = float(input("enter basic salary of employee"))

    hra = 0.2*basic
    da = 0.1*basic
    gross = basic + hra +da
    emp = {
        "name" : name,
        "Basic_Salary" : basic,
        "HRA" : hra,
        "Da" : da,
        "Gross_Salary" : gross
    }
    employee.append(emp)

for i in employee:
    print(i)
    

