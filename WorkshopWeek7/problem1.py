pathFile = input("File Name: ")
openPathFile = open(pathFile)

line = int(input("how many lines: "))
while line!=0:
  for x in openPathFile:
    print(x)
    break
  line-=1
openPathFile.close()