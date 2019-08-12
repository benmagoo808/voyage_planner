"""
This script will batch process downloaded current charts from NOAA for us
stations.
It will rename the file using the following convention :
<Station ID>_<year>.csv
and remove the first row which is just titles for the values

"""

import csv
import os
import re


os.chdir('./current_tables')
for f in os.listdir('.'):
    if not f.startswith('.'):
        stationID = f[:7]
        year = f[-8:]
        path = os.path.split(f)
        os.rename(f, stationID + '_' + year)


#rdr = csv.reader(open('./current_tables/PUG1515_15_Annual_2019.csv', 'rb'))
#writer = csv.writer('./current_tables/PUG1515_2019.csv', 'wb')
