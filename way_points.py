"""
This will be the home of all the data associated with the way points
"""

from datetime import datetime, timedelta
import os
import csv
from vp_data import table_a


class WayPoint:
    """ A class to define way point attributes"""

    def __init__(self, name, distance=0.0, eta=None,
                 current=None, current_direction=None,tide=None,
                 station_id=None, vts=None, country='usa'):
        self.name = name
        self.distance = distance
        self.eta = eta
        self.current = current
        self.current_direction = current_direction
        self.tide = tide
        self.station_id = station_id
        self.vts = vts
        self.country = country

    def get_eta(self, s, d):
        # s = speed in knots, d = departure in datetime. Use Present.Voyage attr
        travel_time = (self.distance * 60) / s
        self.eta = d + timedelta(minutes=travel_time)
        return self.eta

    def get_current(self):
        # Determines the current speed and direction at self.eta
        current_chart = []
        if self.country == 'usa':  # ADD CANADA FUNCTION LATER
            if self.station_id is None:
                self.current_direction = 'Weak and Variable'
                self.current = 0.0
                return self.current, self.current_direction
            else:
                file_obj = open('./current_tables/%s_%s.csv' % (
                    self.station_id, self.eta.year), 'r')
                rdr = csv.reader(file_obj)
                for row in rdr:
                    current_chart.append(row)
                file_obj.close()

                for i in current_chart:
                    # convert time to datetime object, slack to 0 speed
                    i[0] = datetime.strptime(i[0], '%Y-%m-%d %H:%M')
                    if i[2] == '-':
                        i[2] = float(0)
                    i[2] = float(i[2])

                # Compare the eta to find time of nearest max, slack
                for i in range(len(current_chart)):
                    if self.eta > current_chart[i][0]:
                        continue
                    elif self.eta < current_chart[i][0]:
                        upcoming = current_chart[i]
                        previous = current_chart[i-1]
                        break

                # Calculate the current at the eta using the appropriate table
                interval = upcoming[0] - previous[0]
                if previous[2] == 0:
                    time_to_slack = (self.eta - previous[0])
                else:
                    time_to_slack = (upcoming[0] - self.eta)

                for i in range(len(table_a[0])):
                    if table_a[0][i] is None:
                        continue
                    elif interval < table_a[0][i] and i == table_a[0][1]:
                        column = 1
                        break
                    elif interval < table_a[0][i]:
                        x = int(i) - 1
                        if abs(interval - table_a[0][i]) < abs(
                                interval - table_a[0][x]):
                            column = int(i)
                            break
                        else:
                            column = x
                            break

                # Use same approach to find the factor by finding closest row
                for i in range(len(table_a)):
                    if table_a[i][0] is None:
                        continue
                    elif time_to_slack < table_a[i][0] and i == table_a[1][0]:
                        factor = table_a[i][column]
                        break
                    elif time_to_slack < table_a[i][0]:
                        y = int(i) - 1
                        if abs(time_to_slack - table_a[i][0]) < \
                                abs(time_to_slack - table_a[y][0]):
                            r = int(i)
                            factor = table_a[r][column]
                            break
                        else:
                            r = int(y)
                            factor = table_a[r][column]
                            break

                if previous[1] == 'slack':
                    self.current = (upcoming[2] * factor)
                    self.current_direction = upcoming[1]
                else:
                    self.current = (previous[2] * factor)
                    self.current_direction = previous[1]

                return self.current, self.current_direction


class Voyage:
    """ A class to define the attributes of the trip """
    def __init__(self, direction='nb', departure=None, route=None,
                 cruise=9.8, adjspeed=None, position=None, seymour=None):
        self.direction = direction
        self.departure = departure
        self.route = route
        self.cruise = cruise
        self.adjspeed = adjspeed
        self.position = position
        self.seymour = seymour


if __name__ == '__main__':
    # When run for testing only
    west_point = WayPoint('West Point', distance=5, station_id='PUG1515')
    Present = Voyage(departure=datetime.today())
    west_point.get_eta(Present.cruise, Present.departure)
    west_point.get_current()

    print(west_point.eta)
    print(west_point.current)



