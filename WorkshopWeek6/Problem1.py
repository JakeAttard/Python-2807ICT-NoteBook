enterString = input("Enter a string: ")
storingData = []
while enterString:
    storingData.append(enterString)
    enterString = input("Enter a string: ")

storingData.sort()

print(storingData)