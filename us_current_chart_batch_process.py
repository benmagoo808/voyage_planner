"""
This script will batch process downloaded current charts from NOAA for us
stations.
It will rename the file using the following convention :
<Station ID>_<year>.csv
and remove the header row

"""

import csv
import os
import re


os.chdir('./current_tables')  # Cwd to current tables folder


namePattern = re.compile(r'(\w\w\w\d\d\d\d).*(\d\d\d\d\.csv)', re.VERBOSE)


for f in os.listdir('.'):
    if not f.startswith('.'):
        name = namePattern.search(f)
        stationID = name.group(1)
        year = name.group(2)
        os.rename(f, stationID + '_' + year)
        if not f.endswith('.csv'):
            continue

        csvRows = []
        csvFileObj = open(f)
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1 and readerObj:
                continue  # skip first row
            csvRows.append(row)
        csvFileObj.close()

        # Write out the CSV file.
        csvFileObj = open(os.path.join('headerRemoved', f), 'w',
                          newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()

