print("Welcome to the Adder REPL")

def cleanUpWords(s):
    s = s.upper()
    s = s.strip("`\"'.,:;!?_(){}[]")
    return s

createDictValue = dict()

dictInput = input("??? ")


for line in createDictValue:
    words = line.split()
    for word in words:
        cword = cleanUpWords(word)
        createDictValue[cword] = createDictValue.get(cword, 0) + 1

fws = [(fr, w) for (w, fr) in createDictValue.items()]
fws.sort(reverse = True)

for (fr, w) in fws:
    print("{:6d}  {:<}".format(fr, w))
