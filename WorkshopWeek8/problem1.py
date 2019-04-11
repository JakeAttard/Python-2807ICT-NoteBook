while True:
    enterNum = input("List: ")
    n = enterNum.split(' ')
    print(n)
    if len(n) >= 1:
        for i in range(len(n)):
            lowestNumber = min(n)
            highestNumber = max(n)
        print('min = ' + lowestNumber, 'max = ' + highestNumber)
    if not enterNum:
        break