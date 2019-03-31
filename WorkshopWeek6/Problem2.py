numbersList = []

while True:
    enterNumber = input("Enter a number: ")
    if enterNumber == "":
        break
    numbersList.append(enterNumber)

numbersList = sorted(numbersList)

median = 0

if len(numbersList)%2 == 0:
    mid1 = int(len(numbersList)/2+0.5)
    mid2 = int(len(numbersList)/2-0.5)
    median = (int(numbersList[mid1])+int(numbersList[mid2]))/2
else:
    median = numbersList[int(len(numbersList)/2)]

print("Median = " + str(median))