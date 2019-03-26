import math

def calLengthways(L, W):
    lengthTotal = math.ceil(math.ceil(W / rollWidth) * L)
    return lengthTotal

def calWidthways(L, W):
    lengthTotal = math.ceil(math.ceil(L / rollWidth) * W)
    return lengthTotal

rollWidth = 3.66
lengthRoom = 0
widthRoom = 0

roomDimension1 = float(input("Enter room dimension 1 (m): "))
roomDimension2 = float(input("Enter room dimension 2 (m): "))

while True:
    if roomDimension2 <= 0 or roomDimension1 <= 0:
        break
    elif roomDimension2 > roomDimension1:
        lengthRoom = roomDimension2
        widthRoom = roomDimension1
    else:
        length = roomDimension1
        width = roomDimension2

    print("Length = {:.3f}".format(lengthRoom) + " m")
    print("Width = {:.3f}".format(widthRoom) + " m")

    print("Total length required lengthways = ", calLengthways(lengthRoom, widthRoom), " m")
    print("Total length required lengthways = ", calWidthways(lengthRoom, widthRoom), " m")

    roomDimension1 = float(input("Enter room dimension 1 (m): "))
    roomDimension2 = float(input("Enter room dimension 2 (m): "))