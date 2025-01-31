
data = input("Enter  a number :")
try:
    num = int(data)
    print(100 / num)
# except ValueError:
#     print('Invalid Number!')
except Exception as ex:
    print("Error ", ex)
else:
    print("Success")
finally:
    print('Finally!')

print("The End!")




