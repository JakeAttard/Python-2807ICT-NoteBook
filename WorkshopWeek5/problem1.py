strings = str(input("Enter a string: "))
stringlength1 = len(strings)
longstring = strings
stringlength2 = 1
while stringlength2 !=0:
    strings2 = str (input("Enter a string: "))
    stringlength2 = len(strings2)
    if stringlength2 > stringlength1:
        stringlength1 = stringlength2
        strings = strings2
        longstring = strings
    else:
        stringlength1 = stringlength1
        strings = strings
print("longest was: '{}'" .format (longstring))