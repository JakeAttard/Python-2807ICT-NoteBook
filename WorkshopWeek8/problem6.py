from math import sqrt

def dis(t1, t2):
    dis_x = (t2[0] - t1[0]) * 0.5
    dis_y = (t2[1] - t1[1]) * 0.5
    d = sqrt(dis_x ** 2 + dis_y ** 2)
    return d

s = input("Enter the point sequence: ")

l = s.split()
L = []

for e in l:
    if e[0] >= 'A' and e[0] <='Z' and e[1:].isdecimal and int(e[1:]) >= 1 and int(e[1:]) <= 26:
        L.append((ord(e[0]), int(e[1:])))
    else:
        print("Bad Reference: ")
        exit()
dist = 0

for i in range(1, len(L)):
    dist = dist + dis(L[i - 1], L[i])

print("The distance travelled is {:.1f} km".format(dist))