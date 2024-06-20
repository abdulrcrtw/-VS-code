

employee_file = open("employees.text", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()