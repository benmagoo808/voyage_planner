"""
This will scrape and create a current prediction table from the environment
Candada website
"""


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

monthly_tables = {}
result = requests.get("http://www.tides.gc.ca/eng/data/table/2019/"
                      "curr_ref/5000")
src = result.content
soup = BeautifulSoup(src, 'lxml')
months = soup.findAll('caption')

#  Create a dictionary with all the months from the table
for month in soup.findAll('caption'):
    monthly_tables[month.get_text()] = []

    #  Save table for each month as list array in value of each month
    table = month.find_parent('table')
    rows = table.findChildren('tr')
    for row in rows:
        tide = []
        monthly_tables[month.get_text()].append(tide)
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.get_text()
            if value == '\xa0':  # Replaces missing data with None
                value = None
            tide.append(value)

#  remove the two header rows that don't contain 'td' which show as empty lists
for i in monthly_tables.keys():
    monthly_tables[i] = monthly_tables[i][2:]






