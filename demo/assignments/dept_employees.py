
data = [('IT', 'Scott'), ('IT' , 'Mark'), ('SALES', 'James'), ('SALES', 'Anders'),
        ('HR', 'Cathy'), ('HR', 'Roberts') ]

dept = {}

for deptname, empname in data:
    employees = dept.get(deptname, [])
    employees.append(empname)
    dept[deptname] = employees


for deptname, employees in dept.items():
    print(deptname, ",".join(employees))







