# Take basic salary and display net salary
# with 30% HRA and 20% DA

basic = int(input("Enter basic salary :"))
hra = basic * 30 // 100
da = basic * 20 // 100

net_salary = basic + hra + da

print(f'Basic Salary  : {basic:6}')
print(f'HRA           : {hra:6}')
print(f'DA            : {da:6}')
print(f'Net Salary    : {net_salary:6}')

