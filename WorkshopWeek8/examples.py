#Example 1
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#Example 2

# name = input('Enter file:')
# handle = open(name)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(words,0) + 1
#
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount

