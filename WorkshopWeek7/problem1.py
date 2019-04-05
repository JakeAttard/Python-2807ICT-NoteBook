f = open("Lear.txt", "r")
line = int(input("how many lines: "))
while line!=0:
  for x in f:
    print(x)
    break
  line-=1
f.close()