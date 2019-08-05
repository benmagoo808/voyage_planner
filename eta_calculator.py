"""
This script will prompt the user for the estimated avg speed of the vessel
and the estimated departure time from seattle. It will then return a
dictionary with each waypoint being the key and each ETA being the
corresponding value.
"""

# Import from datetime to handle the time adjustments
from datetime import datetime, timedelta


# Define Waypoints as variables for future ease of use in other dicts and lists
SeaHbr = 'Seattle Harbor'
WesPt = 'West Point'
PtNoPt = 'Point No Point'
BushPt = 'Bush Point'
PtPtrg = 'Point Partridge'
BurrIsl = 'Burrows Island'
LawPt = 'Lawrence Point'
PatoIsl = 'Patos Island'
FerrCr = 'Ferry Crossing'
SandHd = 'Sand Heads'
EntIsl = 'Entrance Island'
MerrIsl = 'Merry Island'
CapLzo = 'Cape Lazo'
CapMdg = 'Cape Mudge'
StpIsl = 'Steep Island'
MauIsl = 'Maude Island'
SepHd = 'Separation Head'
CinIsl = 'Cinque Island'
RipPt = 'Ripple Point'
VansPt = 'Vansittart Point'
FanIsl = 'Fanny Island'
BoaHbLt = 'Boat Harbor Light'
LizPt = 'Lizard Point'
JeanIsl = 'Jeannette Island'
CapCau = 'Cape Caution'
DugRk = 'Dugout Rocks'
AddIsl = 'Addenbroke Island'
FogRk = 'Fog Rocks'
PoinIsl = 'Pointer Island'
WalIsl = 'Walker Island'
DryPt = 'Dryad Point'
IdoPt = 'Idol Point'
IvoIsl = 'Ivory Island'
JorPt = 'Jorkins Point'
FrePt = 'Freeman Point'
BoaBlf = 'Boat Bluff'
DitPt = 'Ditmars Point'
SarHd = 'Sarah Head'
GrifPt = 'Griffin Point'
WorIsl = 'Work Island'
KingPt = 'Kingcome Point'
PtCumm = 'Point Cumming'
SainPt = 'Sainty Point'
TomIsl = 'Tom Island'
PitIsl = 'Pitt Island'
BakInl = 'Baker Inlet'
WatRk = 'Watson Rock'
LwyrIsl = 'Lawyer Island'
LucIsl = 'Lucy Island'
HolIsl = 'Holliday Island'
LorRk = 'Lord Rocks'
TreePt = 'Tree Point'
MarIsl = 'Mary Island'
AngPt = 'Angle Point'
MntPt = 'Mountain Point'
Ktn = 'Ketchikan'


# Create a dictionary with the distances from Seattle for every waypoint
DistanceNB = {SeaHbr: 0, WesPt: 5, PtNoPt: 20.6, BushPt: 29.9, PtPtrg: 43.9,
              BurrIsl: 60.5, LawPt: 71.2, PatoIsl: 85, FerrCr: 98,
              SandHd: 107, EntIsl: 126.2, MerrIsl: 139, CapLzo: 177.2,
              CapMdg: 199, StpIsl: 204.5, MauIsl: 209.5, SepHd: 212.1,
              CinIsl: 219.2, RipPt: 228, VansPt:234.2, FanIsl: 245.7,
              BoaHbLt: 268.1, LizPt: 284.3, JeanIsl: 309.1, CapCau: 329.8,
              DugRk: 342.9, AddIsl: 357.2, FogRk: 379.6, PoinIsl: 385.4,
              WalIsl: 392.9, DryPt: 398.7, IdoPt: 405.8, IvoIsl: 410.9,
              JorPt: 424.4, FrePt: 431.4, BoaBlf: 437, DitPt: 442.5,
              SarHd: 452.1, GrifPt: 463, WorIsl: 471.6, KingPt: 482.5,
              PtCumm: 490.5, SainPt: 498.5, TomIsl: 513.5, PitIsl: 525.7,
              BakInl: 533.9, WatRk: 544.2, LwyrIsl: 557.7, LucIsl: 572.4,
              HolIsl: 593, LorRk: 599.6, TreePt: 605.6, MarIsl: 625.8,
              AngPt: 638, MntPt: 643.5, Ktn: 648}

# Get speed and time
print('What is your Estimated Speed in Knots?')
EstimatedSpeed = float(input()) ### ADD VALIDATION
print('What time will you be leaving today? (in HHMM format)')
DepartureHHMM = input()  ### ADD VALIDATION


# Take the hours and minutes from the input and converts to int
DepartureHour = int(DepartureHHMM[:2])
DepartureMin = int(DepartureHHMM[2:])
# Convert ETD to a datetime object
today = datetime.today()  # create a datetime object for today to get full date
EstimatedDeparture = datetime(today.year, today.month, today.day,
                              DepartureHour, DepartureMin)


"""Define a function that iterates through DistanceNB and calculates the eta
Then store that in a new dictionary called CalculatedETA
"""


def get_eta(s, t):
    #  s, is speed in knots as float or int, t is departure time as datetime
    calculated_eta = {}
    for k, v in DistanceNB.items():
        travel_time = (v * 60) / s  # Distance * 60 / speed = time in minutes
        eta = t + timedelta(minutes=travel_time)
        calculated_eta[k] = eta  # Add current key and new eta as key:value
    return calculated_eta


# Run function and save as new dict
CalculatedETA = get_eta(EstimatedSpeed, EstimatedDeparture)

# Convert datetime objects to strings and print as separate lines
for k, v in CalculatedETA.items():
    print('You will arrive at ' + k + ' on ' + str(v))
