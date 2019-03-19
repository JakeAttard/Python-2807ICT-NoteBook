rugbyTeam = 15
bigBuses = 48
smallBuses = 10
costBigBuses = 200.00
costSmallBuses = 95.00

rugbyTeam = rugbyTeam*int(input("How many teams? "))

if(rugbyTeam%bigBuses)>= 20:
    print("Hire ", rugbyTeam // bigBuses + 1, "big buses and", 0, "small buses")
    print("Cost = $", (rugbyTeam // bigBuses+1)*costBigBuses)
else:
    print("Hire ", rugbyTeam // bigBuses, "big buses and", (rugbyTeam % bigBuses // smallBuses)+1, "small buses")
    print("Cost = $", ((rugbyTeam // bigBuses) * costBigBuses) + ((rugbyTeam % bigBuses // smallBuses)+1)*costSmallBuses)