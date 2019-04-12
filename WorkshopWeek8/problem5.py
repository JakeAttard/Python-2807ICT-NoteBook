def function(list, diff):
    counter = 1
    for a in list[::2]:
        for b in list[1::2]:
            if int(b) - int(a) == diff:
                counter += 1
            elif int(b) - int(a) == -1 * diff:
                counter += 1
            else:
                break
    return counter

def testString(a):
    list1 = a.split()
    if len(a) == 1:
        print(1)
    elif len(a) == 0:
        exit()
    else:
        difference = int(list1[1]) - int(list1[0])
        print(function(list1, difference))


a = input("List: ")
testString(a)
while len(a) != 0:
    a = input("List: ")
    testString(a)