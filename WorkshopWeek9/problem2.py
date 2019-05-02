def cal (sons,daughters):
    d['daughter/s'] = int(daughters)
    d['son/s'] = int(sons)
    d['children'] = d ['son/s'] + d['daughter/s']
    return d ['children']
print ("Welcome to the adder REPEL. ")
d = dict()
sons = input("Enter value for son/s: ")
daughters = input("Enter value for daughter/s: ")
print("Children equals ", cal (sons, daughters))