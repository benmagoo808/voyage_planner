"""
This will keep the lists which we can use to give the way points attributes
"""

from datetime import datetime, timedelta

names = ['Seattle', 'West Point', 'Point No Point', 'Bush Point',
         'Point Partridge', 'Burrows Island', 'Lawrence Point',
         'Patos Island', 'Ferry Crossing', 'Sand Heads', 'Entrance Island',
         'Merry Island', 'Cape Lazo', 'Cape Mudge', 'Steep Island',
         'Maude Island', 'Separation Head', 'Cinque Island', 'Ripple Point',
         'Vansittart Point', 'Fanny Island', 'Boat Harbor Light',
         'Lizard Point', 'Jeannette Island', 'Cape Caution', 'Dugout Rocks',
         'Addenbroke Island', 'Fog Rocks', 'Pointer Island',
         'Walker Island', 'Dryad Point', 'Idol Point', 'Ivory Island',
         'Jorkins Point', 'Freeman Point', 'Boat Bluff', 'Ditmars Point',
         'Sarah Head', 'Griffin Point', 'Work Island', 'Kingcome Point',
         'Point Cumming', 'Sainty Point', 'Tom Island', 'Pitt Island',
         'Baker Inlet', 'Watson Rock', 'Lawyer Island', 'Lucy Island',
         'Holliday Island', 'Lord Rocks', 'Tree Point', 'Mary Island',
         'Angle Point', 'Mountain Point', 'Ketchikan']

dist_from_sea = [0, 5, 20.6, 29.9, 43.9, 60.5, 71.2, 85, 98, 107, 126.2, 139,
                 177.2, 199, 204.5, 209.5, 212.1, 219.2, 228, 234.2, 245.7,
                 268.1, 284.3, 309.1, 329.8, 342.9, 357.2, 379.6, 385.4,
                 392.9, 398.7, 405.8, 410.9, 424.4, 431.4, 437, 442.5,
                 452.1, 463, 471.6, 482.5, 490.5, 498.5, 513.5, 525.7,
                 533.9, 544.2, 557.7, 572.4, 593, 599.6, 605.6, 625.8,
                 638, 643.5, 648]

table_a = (
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

""" Temp lists for testing """

wa_names = ['Seattle', 'West Point', 'Point No Point', 'Bush Point',
            'Point Partridge', 'Burrows Island', 'Lawrence Point',
            'Patos Island']

wa_dist = dist_from_sea[:8]

current_station_id = (None, 'PUG1515', 'PUG1606', 'PUG1617', 'PUG1708',
                      'PUG1714', 'PCT1466', 'PCT2011')
