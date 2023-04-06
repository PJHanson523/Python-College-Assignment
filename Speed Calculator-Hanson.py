'''Python code for calculating speed in knots, miles per hour, or feet per second given both "Miles" and "Hours"

[[[UPDATE NEEDED: Please change data types from integers to floating or decimal when available to ensure accurate
calculations of all data types]]]
'''

print("")
print('WELCOME TO THE SPEED CALCULATOR! [created by me]')
print("")
print('To calculate the correct speeds, please have the distance as miles and the time as hours.')
print("")
Yes = input("When you are ready, please press the 'y' button on your keybaord and hit enter. ")

if Yes == "y":
    Milesinput = input("How many miles? ")
    Hoursinput = input("For how many hours? ")
    print(" ")

    Miles = int(Milesinput)
    Hours = int(Hoursinput)
    Knots = (Miles / 1.15078)
    Feet = (Miles * 5280)
    Seconds = (Hours * 3600)
    Knotspeed = (Knots / Hours)
    MPR = (Miles / Hours)
    FPS = (Feet / Seconds)

    print("The speed in knots is:", Knotspeed)
    print("The speed in miles per hour is:", MPR)
    print("The speed in feet per second is:", FPS