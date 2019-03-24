def enterString():
    enterString(bool)
while True:
    enterString = input("Enter a string: ")
    for i in str(enterString):
        if i.isdigit():
            print("Has no digits: ", False)
            break
        else:
            print("Has no digits: ", True)
