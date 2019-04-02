numbersList = []

while True:
    enterNumber = input("Enter a number: ")
    if enterNumber == "":
        break
    numbersList.append(enterNumber)

numbersList = sorted(numbersList)

median = 0

if len(numbersList)%2 == 0:
    middle1 = int(len(numbersList)/2+0.5)
    middle2 = int(len(numbersList)/2-0.5)
    median = (int(numbersList[middle1])+int(numbersList[middle2]))/2
else:
    median = numbersList[int(len(numbersList)/2)]

print("Median = " + str(median))