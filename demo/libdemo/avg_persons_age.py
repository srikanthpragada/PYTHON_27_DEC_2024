import json

f = open("persons.json", "rt")
# read the data from the file
data = f.read()
# convert json array to list of dict
persons = json.loads(data)
f.close()
# total = 0
# for person in persons:
#     total += person['age']

total = sum(map(lambda p : p['age'], persons))
print(total // len(persons))
