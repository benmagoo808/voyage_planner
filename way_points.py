"""
This will be the home of all the data associated with the way points
"""

from datetime import datetime, timedelta


class WayPoint:
    """ A class to define way point attributes"""

    def __init__(self, name, distance=0.0, eta=None,
                 current=None, tide=None, station_id=None, vts=None,
                 country=None ):
        self.name = name
        self.distance = distance
        self.eta = eta
        self.current = current
        self.tide = tide
        self.station_id = station_id
        self.vts = vts
        self.country = country


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
    west_point = WayPoint('West Point', 5)
    sea = WayPoint('Seattle', 0)
    print(west_point.name, west_point.distance_nb)
    temp = [west_point, sea]
    print(temp)


