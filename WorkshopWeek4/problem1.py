maxSeats = 100

groupSize = int(input("Seats remaining: {}" ". How many people do you have in your group?" .format(maxSeats)))

def calc(groupSize, maxSeats):
    if groupSize < maxSeats:
        print("Booked, thank you")
        maxSeats = maxSeats - groupSize
        groupSize = int(input("Seats remaining: {}" ". How many people do you have in your group?".format(maxSeats)))
        calc(groupSize, maxSeats)
    elif groupSize == maxSeats:
        print("Booked, thank you")
        print("SOLD OUT!")
        exit()
    else:
        print("Sorry, not enough seats left.")
        groupSize = int(input("Seats remaining: {}" ". How many people do you have in your group?".format(maxSeats)))
        calc(groupSize, maxSeats)
calc(groupSize, maxSeats)