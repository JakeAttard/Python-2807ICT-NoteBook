def createListSet1(a):
    list = a.split()
    listSet1 = {100}
    for i in list:
        listSet1.add(i)
    return listSet1

def createListSet2(a):
    list2 = a.split()
    listSet2 = {100}
    for i in list2:
        listSet2.add(i)
    return listSet2

while True:
    a = input("List 1:")
    if len(a)==0:
        exit()
    else:
        b = input("List 2: ")
        print(list(createListSet1(a).difference(createListSet2(b))))