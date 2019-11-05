filename = input("Enter order filename: ")
f = open(filename)
totalPrice = 0.00
totalWeight = 0
for line in f:
    words = line.split()
    num = int(words[0])
    totalPrice += float(words[-2][1:]) * num
    totalWeight += int(words[-1]) * num
print("Items total price = ${:.2f}".format(totalPrice))
print("Total weight = {:.1f} kg".format(totalWeight / 1000.0))
postage = (totalWeight + 999) // 1000 * 10.50
print("Postage = ${:.2f}".format(postage))
print("Order total price = ${:.2f}".format(totalPrice + postage))