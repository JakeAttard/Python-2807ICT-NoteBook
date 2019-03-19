num = int(input("How many lines?"))
row = 1
for i in range(0,num):
    for j in range(0,row):
        print("#", end="")
    row+=row
    print()