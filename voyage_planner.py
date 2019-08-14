"""
This program will generate a voyage plan for the inside passage to Alaska with
tide, current, and weather information, based on the users input.
"""


from datetime import datetime, timedelta
from vp_data import wa_dist, wa_names, current_station_id
from way_points import WayPoint, Voyage


def get_speed():
    """ This gets the departure speed """
    while True:
        try:
            # Take speed and validate through comparison and conversion
            print('What is your Estimated Speed in Knots? (##.# Format')
            input_speed = float(input())
            if input_speed != 0:
                break
            else:
                print("You'll never make it to Alaska at that speed")
                continue
        except ValueError:
            print("Your estimated speed must be in numerical form")
            continue
    return input_speed


def get_departure():
    """ This gets the departure time of same day """
    while True:
        errormsg = "Your departure time must be four numerical digits. \nTwo " \
                   "digits for the hours and two for the minutes. Military " \
                   "style. \nPlease try again. "
        # Get departure time as a string, validate, convert back for later slice
        try:
            print('What time will you be leaving today? (in HHMM format)')
            input_departure = input()
            if len(input_departure) != 4:
                print(errormsg)
                continue
            else:
                input_departure = int(input_departure)
                input_departure = str(input_departure)
                break
        except ValueError:
            print(errormsg)

    # Slice the input and convert to int
    dep_hour = int(input_departure[:2])
    dep_min = int(input_departure[2:])

    # Convert ETD to a datetime object
    today = datetime.today()
    etd = datetime(today.year, today.month, today.day, dep_hour,
                    dep_min)
    return etd


est_speed = get_speed()
est_departure = get_departure()

PresentVoyage = Voyage(departure=est_departure, cruise=est_speed)

waypoints = {name: WayPoint(name) for name in wa_names}

count = 0
for v in waypoints.values():
    v.distance = wa_dist[count]
    v.station_id = current_station_id[count]
    v.get_eta(s=PresentVoyage.cruise, d=PresentVoyage.departure)
    v.get_current()
    print('You will arrive at %s at %s. The current will be %s knots%s' % (
        v.name, v.eta, v.current, v.current_direction))
    count += 1

