# x = ['ab', 'cd']
#
# for i in x:
#     i.isupper()
# print(x)

#sum = 0
#item = 0
#while item < 5:
#    item += 1
#    sum += item
#    if sum >= 4: continue

#i = 5
#while True:
#    if i%9 == 0:
#        break
 #   print(i, end='')
  #  i += 1
sum = 0
for i in range(10,20):
    for j in range(i):
        print(i+j)
        sum+=1
print(sum)