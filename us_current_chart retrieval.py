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


