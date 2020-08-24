employee_file = open("files/employees.txt", "r")
print(employee_file.readable())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
