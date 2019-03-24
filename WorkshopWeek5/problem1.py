print("Enter String",end=":")
a = input ()
b = a
while len(a) != 0:
    if a > b:
        a=b
    else:
        print("enter a string", end=":")
        a = input()
if len (a) ==0:
    print("Largest string: '"+b+"'")