from blacklist import*

BLdns = Blacklist()

while True:
    CommandDNS = input(">>>")
    Command = CommandDNS.split()
    if Command[0] == "blacklist":
        BLdns.newblacklist(Command[1])
    elif len(Command) == 2:
        if "find" in Command:
            print(BLdns.domainlookup(Command[1]))
    elif len(Command) == 3:
        if "change" in Command:
            print(BLdns.upDateDomain(Command[1],Command[2]))
        elif "add" in Command:
            print(BLdns.change(Command[1],Command[2]))

    else:
        print("Error")