pathFile = input("File Name: ")
openPathFile = open(pathFile)
words = 0
characters = 0
lines = 0

for x in openPathFile:
    for word in x.split():
        words += 1
    lines += 1
    characters += len(x)

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
openPathFile.close()



# txt = open("Lear.txt", "r")
# words = 0
# characters = 0
# lines = 0
#
# for x in txt:
#     for word in x.split():
#         characters += len(word)
#         words += 1
#     lines += 1
#
#
# print("Characters:", characters)
# print("Words:", words)
# print("Lines:", lines)
# txt.close()