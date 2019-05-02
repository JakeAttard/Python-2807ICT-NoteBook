#wordsFreq
#Reads a file and prints the unique words and how often they occured in decreasing order of frequency.

def cleanUpWords(s):
    s = s.upper()
    s = s.strip("`\"'.,:;!?_(){}[]")
    return s

freqs = dict() #words -> frequencies
path = input("Enter a filename: ")
f = open(path)

for line in f:
    words = line.split()
    for word in words:
        cword = cleanUpWords(word)
        freqs[cword] = freqs.get(cword, 0) + 1
f.close()

fws = [(fr, w) for (w, fr) in freqs.items()]
fws.sort(reverse = True)

for (fr, w) in fws:
    print("{:6d}  {:<}".format(fr, w))