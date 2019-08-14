"""
This program will generate a voyage plan for the inside passage to Alaska with
tide, current, and weather information, based on the users input.
"""


from datetime import datetime, timedelta


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


def get_eta(s, d, distance):
    travel_time = (distance * 60) / s
    eta = d + timedelta(minutes=travel_time)
    print(eta)
    return eta


est_speed = get_speed()
est_departure = get_departure()
arrival = get_eta(est_speed, est_departure, 98)