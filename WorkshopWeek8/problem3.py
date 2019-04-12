def createList(a):
    list1 =[]
    list2 =[]
    multiplelist = []
    collectiveList = a.split()
    reverseCollectiveList = collectiveList[::-1]
    for i in collectiveList:
        if len(i) ==2:
            if ';' in i:
                list1.append(i[0])
                break
        else:
            list1.append(i)

    for i in reverseCollectiveList:
        if len(i) == 2:
            if ';' in i:
                list2.append(i[0])
                break
        else:
            list2.append(i)
    for element in list1:
        num1 = list1.count(element)
        if element in list2:
            num2 = list2.count(element)
            if num1 >= 2 and num2 >= 2:
                multiplelist.append(element)
    multiplelist.sort()
    return  multiplelist

def createSet(finalList):
    set = {100}
    for i in finalList:
        set.add(i)
    set.remove(100)
    list(set).sort()
    return list(set)

a = input("Lists: ")
if len(a)==0:
    exit()
else:
    print(createSet(createList(a)))
while True:
    a = input("Lists: ")
    if len(a) == 0:
        exit()
    else:
        print(createSet(createList(a)))