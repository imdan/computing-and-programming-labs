day = input("Enter the day the call started at: ")

time = int(input("Enter the time the call started at (hhmm): "))

duration = int(input("Enter the duration of the call (in minutes): "))

if (day == "Sat" or day == "Sun"):
    cost = duration * .15
else:
    if (800 <= time <= 1800):
        cost = duration * .4
    else:
        cost = duration * .25

print("This call will cost ${:2.2f}".format(cost))
