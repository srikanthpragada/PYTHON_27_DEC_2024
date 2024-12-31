# Take price and display net price after a discount of 15%

# input
data = input("Enter price :")
price = int(data)  # convert str to int

# process
discount = price * 15 // 100
net_price = price - discount

# output
print(net_price)
