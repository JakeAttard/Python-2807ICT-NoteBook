while True:
    enterString = input("Enter a string: ")

    stringlist = []

    for i in enterString:
        stringlist.append(i)
    stringlist.reverse()

    reverse = ''.join(stringlist)

    if not stringlist:
        break
    elif reverse == enterString:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")