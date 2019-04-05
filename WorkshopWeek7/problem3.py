import statistics
pathFile = input("File Name: ")
openPathFile = open(pathFile)

arrayList = []
sum = 0
numLines = 0

for x in openPathFile:
    numLines += 1
    sum += float(x)
    arrayList.append(float(x))
    avg = sum/numLines
arrayList.sort()
print("Average = {:.1f}".format(avg))
print("Median =", statistics.median(arrayList))

openPathFile.close()