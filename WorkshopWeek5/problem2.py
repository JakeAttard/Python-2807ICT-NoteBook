def enterString(String):
    bool = 1
    for i in str(String):
        if i.isdigit():
            bool = 0
            break
        else:
            bool = 1
    return bool
while True:
    String = input("Enter a string: ")
    enterString(String)
    if enterString(String) == 0:
        print("Has no digits: False")
    elif enterString(String) ==1:
        print("Has no digits: True")