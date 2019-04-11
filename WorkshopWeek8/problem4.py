def function(list, diff):
    state = 0
    for a in list[::2]:
        for b in list[1::2]:
            if int(b) - int(a) == diff:
                state = 1
            elif int(b) - int(a) == -1 * diff:
                state = 1
            else:
                state = 0
                break
    return state

def testString(a):
    list1 = a.split()
    if len(a) == 1:
        print("False")
    elif len(a) == 0:
        exit()
    else:
        difference = int(list1[1]) - int(list1[0])
        if function(list1, difference) == 0:
            print("False")
        else:
            print("True")


a = input("List: ")
testString(a)
while len(a) != 0:
    a = input("List: ")
    testString(a)