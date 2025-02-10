import requests

# Get data from Github REST API
resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print("Sorry! Invalid username!")
    exit(0)


details = resp.json()   # Covert JSON to dict

print(f"Name    : {details['name']}")
print(f"Company : {details['company']}")
print(f"Location: {details['location']}")


