"""
This script will open the corresponding yearly current chart for a given
station ID and find the closest slack water and max current, then interpolate
the current speed and direction from those values for a given eta

"""

from datetime import datetime, timedelta
import csv


eta = datetime(2019, 5, 26, 8, 36)  # Define an eta in format we are using
DistanceNB = {'West Point': eta}  # dummy dict that will be our eta dict
current_chart = []  # list we will fill from the .csv file
current = []  # our future list with actual current speed
upcoming = []  # our future list with details about next current stage
previous = []  # our future list with details about the previous current stage


# Create a table of factors for current at any time from nearest max and slack
# Every nested tuple is a row, same index in each row is a column
tableA = (
    (None, timedelta(hours=1, minutes=20), timedelta(hours=1, minutes=40),
     timedelta(hours=2), timedelta(hours=2, minutes=20),
     timedelta(hours=2, minutes=40), timedelta(hours=3),
     timedelta(hours=3, minutes=20), timedelta(hours=3, minutes=40),
     timedelta(hours=4), timedelta(hours=4, minutes=20),
     timedelta(hours=4, minutes=40), timedelta(hours=5),
     timedelta(hours=5, minutes=20), timedelta(hours=5, minutes=40)),
    (timedelta(minutes=20), 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1),
    (timedelta(minutes=40), 0.7, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.2,
     0.2, 0.2, 0.2, 0.2),
    (timedelta(hours=1), 0.9, 0.8, 0.7, 0.6, 0.6, 0.5, 0.5, 0.4, 0.4, 0.4, 0.3,
     0.3, 0.3, 0.3),
    (timedelta(hours=1, minutes=20), 1.0, 1.0, 0.9, 0.8, 0.7, 0.6, 0.6, 0.5,
     0.5, 0.5, 0.4, 0.4, 0.4, 0.4),
    (timedelta(hours=1, minutes=40), None, 1.0, 1.0, 0.9, 0.8, 0.8, 0.7, 0.7,
     0.6, 0.6, 0.5, 0.5, 0.5, 0.4, 0.4),
    (timedelta(hours=2), None, None, 1.0, 1.0, 0.9, 0.9, 0.8, 0.8, 0.7, 0.7,
     0.6, 0.6, 0.6, 0.5),
    (timedelta(hours=2, minutes=20), None, None, None, 1.0, 1.0, 0.9, 0.9, 0.8,
     0.8, 0.7, 0.7, 0.7, 0.6, 0.6,),
    (timedelta(hours=2, minutes=40), None, None, None, None, 1.0, 1.0, 1.0, 0.9,
     0.9, 0.8, 0.8, 0.7, 0.7, 0.7),
    (timedelta(hours=3), None, None, None, None, None, 1.0, 1.0, 1.0, 0.9, 0.9,
     0.8, 0.8, 0.8, 0.7),
    (timedelta(hours=3, minutes=20), None, None, None, None, None, None, 1.0,
     1.0, 1.0, 0.9, 0.9, 0.9, 0.8, 0.8),
    (timedelta(hours=3, minutes=40), None, None, None, None, None, None, None,
     1.0, 1.0, 1.0, 0.9, 0.9, 0.9, 0.9),
    (timedelta(hours=4), None, None, None, None, None, None, None, None, 1.0,
     1.0, 1.0, 1.0, 0.9, 0.9),
    (timedelta(hours=4, minutes=20), None, None, None, None, None, None, None,
     None, None, 1.0, 1.0, 1.0, 1.0, 0.9),
    (timedelta(hours=4, minutes=40), None, None, None, None, None, None, None,
     None, None, None, 1.0, 1.0, 1.0, 1.0),
    (timedelta(hours=5), None, None, None, None, None, None, None, None, None,
     None, None, 1.0, 1.0, 1.0),
    (timedelta(hours=5, minutes=20), None, None, None, None, None, None, None,
     None, None, None, None, None, 1.0, 1.0),
    (timedelta(hours=5, minutes=40), None, None, None, None, None, None, None,
     None, None, None, None, None, None, 1.0)
)


for k, v in DistanceNB.items():  # loop through and open corresponding table
    rdr = csv.reader(open('./current_tables/%s_%s.csv' % (k, v.year)))
    for row in rdr:  # convert rows to list items
        current_chart.append(row)


for i in current_chart:
    i[0] = datetime.strptime(i[0], '%Y-%m-%d %H:%M')  # Convert string->datetime
    if i[2] == '-':  # convert dashes for slack to 0 speed
        i[2] = float(0)
    i[2] = float(i[2])  # convert strings to floats for math


# Compare the eta to find time of closest max and slack, speed of max current
for i in range(len(current_chart)):  # iterate through list using index
    if eta > current_chart[i][0]:  # if eta is past table entry, continue
        continue
    elif eta == current_chart[i][0]:  # if eta is same, current is as listed
        current = current_chart[i[1:]]
        break
    elif eta < current_chart[i][0]:  # if eta is less than get previous and next
        upcoming = current_chart[i]
        i -= 1
        previous = current_chart[i]
        break


# Calculate the current at the eta using the appropriate table
interval = upcoming[0] - previous[0]  # find time difference between stages
if previous[2] == 0:                  # if previous stage was slack
    timeToSlack = (eta - previous[0])  # find time difference between slack/eta
else:                                 # otherwise upcoming is slack
    timeToSlack = (upcoming[0] - eta)  # reverse order to get positive number


for i in range(len(tableA[0])):  # find closest column
    if tableA[0][i] is None:  # skip the none values
        continue
    elif interval < tableA[0][i] and i == tableA[0][1]:
        column = 1  # If it's less than column [1] it's closest to column [1]
        break
    elif interval < tableA[0][i]:  # Find the first higher value
        x = int(i) - 1             # and index of lower value
        if abs(interval - tableA[0][i]) < abs(interval - tableA[0][x]):
            column = int(i)  # find closest to interval, set column as row index
            break
        else:
            column = x  # find closest to interval, set column as row index
            break


# Use same approach to find the factor by finding closest row
for i in range(len(tableA)):
    if tableA[i][0] is None:
        continue
    elif timeToSlack < tableA[i][0] and i == tableA[1][0]:
        factor = tableA[i][column]  # if less than row 1 it's row 1
        break
    elif timeToSlack < tableA[i][0]:  # compare as before
        y = int(i) - 1
        if abs(timeToSlack - tableA[i][0]) < abs(timeToSlack - tableA[y][0]):
            r = int(i)
            factor = tableA[r][column]
            break
        else:
            r = int(y)
            factor = tableA[r][column]  # factor is intersection of row/column
            break


if previous[1] == 'slack':          # apply factor to the closest max current
    presentCurrent = (upcoming[2] * factor)
    stage = upcoming[1]
else:
    presentCurrent = (previous[2] * factor)
    stage = previous[1]

print('The current at West Point is %s knots%s at your ETA of %s' %
      (str(presentCurrent), stage, str(eta)))
