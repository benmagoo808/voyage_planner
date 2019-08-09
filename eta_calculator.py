"""
This script will prompt the user for the estimated avg speed of the vessel
and the estimated departure time from seattle. It will then return a
dictionary with each way point being the key and each ETA being the
corresponding value.
"""

# Import from datetime to handle the time adjustments
from datetime import datetime, timedelta

WayPoints = ['Seattle', 'West Point', 'Point No Point', 'Bush Point',
             'Point Partridge', 'Burrows Island', 'Lawrence Point',
             'Patos Island', 'Ferry Crossing', 'Sand Heads', 'Entrance Island',
             'Merry Island', 'Cape Lazo', 'Cape Mudge', 'Steep Island',
             'Maude Island', 'Separation Head', 'Cinque Island', 'Ripple Point',
             'Vansittart Point', 'Fanny Island', 'Boat Harbor Light',
             'Lizard Point', 'Jeannette Island', 'Cape Caution', 'Dugout Rocks',
             'Addenbroke Island', 'Fog Rocks', 'Pointer Island',
             'Walker Island', 'Dryad Point', 'Idol Point', 'Ivory Island',
             'Jorkins Point', 'Freeman Point', 'Boat Bluff', 'Ditmars Point',
             'Sarah Head', 'Griffin Point', 'Work Island', 'Kingcome Point',
             'Point Cumming', 'Sainty Point', 'Tom Island', 'Pitt Island',
             'Baker Inlet', 'Watson Rock', 'Lawyer Island', 'Lucy Island',
             'Holliday Island', 'Lord Rocks', 'Tree Point', 'Mary Island',
             'Angle Point', 'Mountain Point', 'Ketchikan']

DistancesFromSEA = [0, 5, 20.6, 29.9, 43.9, 60.5, 71.2, 85, 98, 107, 126.2, 139,
                    177.2, 199, 204.5, 209.5, 212.1, 219.2, 228, 234.2, 245.7,
                    268.1, 284.3, 309.1, 329.8, 342.9, 357.2, 379.6, 385.4,
                    392.9, 398.7, 405.8, 410.9, 424.4, 431.4, 437, 442.5,
                    452.1, 463, 471.6, 482.5, 490.5, 498.5, 513.5, 525.7,
                    533.9, 544.2, 557.7, 572.4, 593, 599.6, 605.6, 625.8,
                    638, 643.5, 648]

# zip the lists into a dictionary
DistanceNB = dict(zip(WayPoints, DistancesFromSEA))

# Get speed and time
while True:  # Loop that restarts input if not valid
    try:
        print('What is your Estimated Speed in Knots? (##.# Format')
        EstimatedSpeed = float(input())
        if EstimatedSpeed != 0:  # 0 Speed will cause division errors later
            break  # exits loop unless value error detected below
        else:
            print("You'll never make it to Alaska at that speed")
            continue  # restarts loop
    except ValueError:  # Conversion to float will fail if not numerical
        print("Your estimated speed must be in numerical form")
        continue


while True:  # same test as above, except checking for length of 4 instead of 0
    errormsg = "Your departure time must be four numerical digits. \nTwo " \
               "digits for the hours and two for the minutes. Military " \
               "style. \nPlease try again. "
    try:
        print('What time will you be leaving today? (in HHMM format)')
        DepartureHHMM = input()
        if len(DepartureHHMM) != 4:
            print(errormsg)
            continue
        else:
            DepartureHHMM = int(DepartureHHMM)  # Check for numerical input
            DepartureHHMM = str(DepartureHHMM)  # Convert back so we can slice
            break
    except ValueError:
        print(errormsg)

# Take the hours and minutes from the input and converts to int
DepartureHour = int(DepartureHHMM[:2])
DepartureMin = int(DepartureHHMM[2:])

# Convert ETD to a datetime object
today = datetime.today()  # create a datetime object for today to get full date
EstimatedDeparture = datetime(today.year, today.month, today.day,
                              DepartureHour, DepartureMin)

# Define a function that iterates through DistanceNB and calculates the eta's


def get_eta(s, t):
    #  s, is speed in knots as float or int, t is departure time as datetime
    calculated_eta = {}
    for k, v in DistanceNB.items():
        travel_time = (v * 60) / s  # Distance * 60 / speed = time in minutes
        eta = t + timedelta(minutes=travel_time)
        calculated_eta[k] = eta  # Add current key and new eta as key:value
    return calculated_eta


# Run function and save as new dict
CalculatedETA = get_eta(EstimatedSpeed, EstimatedDeparture)

# Convert datetime objects to strings and print as separate lines
for k, v in CalculatedETA.items():
    print('You will arrive at ' + k + ' on ' + v.strftime("%A, at %H:%M"))
