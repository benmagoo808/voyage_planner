"""
This script will open the corresponding yearly current chart for a given
station ID and find the closest slack water and max current, then interpolate
the current speed and direction from those values for a given eta

"""

from datetime import datetime, timedelta

import csv

eta = datetime(2019,8,10,12,00)  # Define an eta in format we are using
DistanceNB = {'West Point': eta}  # dummy dict that will be our eta dict
current_chart = []


for k, v in DistanceNB.items():  # loop through and open corresponding table
    rdr = csv.reader(open('./current_tables/%s_%s.csv' % (k, v.year)))
    for row in rdr:  # convert rows to list items
        current_chart.append(row)

for i in current_chart:
    i[0] = datetime.strptime(i[0], '%Y-%m-%d %H:%M')  # Convert string->datetime
    if i[2] == '-':  # convert dashes for slack to 0 speed
        i[2] = 0
    i[2] = float(i[2])  # convert strings to floats for math

print(current_chart)
# Compare the eta to the current chart and get closest slack and max, max value

for i in range(len(current_chart)):  # iterate through list using index
    if eta > current_chart[i][0]:  # if eta is past table entry, continue
        continue
    elif eta == current_chart[i][0]:  # if eta is same, current is as listed
        current = current_chart[i[1:]]
    elif eta < current_chart[i][0]:  # if eta is less than get previous and next
        upcoming = current_chart[i]
        i -= 1
        previous = current_chart[i]
        break

print(previous)
print(upcoming)