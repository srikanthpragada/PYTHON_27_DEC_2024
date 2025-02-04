import os

entries = os.walk(r'c:\classroom\dec27\demo')

count = 0
for (dirname, dirs, files) in entries:
    for file in files:
        if file.endswith('.py'):
            print(dirname + "\\" + file)
            count += 1

print(f"Count = {count}")
