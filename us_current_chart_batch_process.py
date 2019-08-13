"""
This script will batch process downloaded current charts from NOAA for US
stations.
It will rename the file using the following convention :
<Station ID>_<year>.csv
and remove the header row from the csv file if one is present

"""

import csv
import os
import re


os.chdir('./current_tables')  # Cwd to current tables folder

# Regex pattern pulls the groups we want from the downloaded format
namePattern = re.compile(r'(\w\w\w\d\d\d\d).*(20\d\d).*(\.csv)',
                         re.VERBOSE)
yearPattern = re.compile(r'20\d\d.*')  # pattern for data instead of header


for f in os.listdir('.'):  # iterate through the files in dir
    if not f.startswith('.'):  # unless they are hidden files
        name = namePattern.search(f)  # grab the patterns we want from the name
        stationID = name.group(1)
        year = name.group(2)
        ext = name.group(3)
        os.rename(f, stationID + '_' + year + ext)  # rename using our format


for f in os.listdir('.'):  # iterate through the files in dir
    if f.endswith('.csv'):  # that are .csv
        csvRows = []
        fileObj = open(f, 'r')  # open each file
        reader = csv.reader(fileObj)  # read it with csv.reader
        for row in reader:
            year = yearPattern.search(row[0])  # check if first line is data
            if year is None:  # if not, skip write to csvRows
                continue
            else:
                csvRows.append(row)  # if data, write to csvRows

        fileObj.close()  # close file

        fileObj = open(f, 'w', newline='')  # open again in write mode
        writer = csv.writer(fileObj)
        for row in csvRows:
            writer.writerow(row)  # write each row from csvRows to the file
        fileObj.close()  # close file


print('Batch editing complete!')