"""
This script will batch process downloaded current charts from NOAA for us
stations.
It will rename the file using the following convention :
<Station ID>_<year>.csv
and remove the first row which is just titles for the values

"""

import csv
import sys


rdr = csv.reader(open('./current_tables/PUG1515_15_Annual_2019.csv', 'rb'))
writer = csv.writer('./current_tables/PUG1515_2019.csv', 'wb')


if rdr