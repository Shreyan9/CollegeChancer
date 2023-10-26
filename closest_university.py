import math
import csv
import sys


def distance(origin, destination):
    """
    Calculate the Haversine distance.
    From: https://stackoverflow.com/a/38187562/1561431
    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)
    Returns
    -------
    distance_in_km : float
    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def closest_university(location):
    dist = sys.float_info.max
    uni= ""
    csv_file = csv.DictReader(open('university-data.csv'))
    for row in csv_file:
        if row['LATITUDE'] == '-' or row['LONGITUDE'] == '-':
            pass
        else:
            tuple = float(row['LATITUDE']), float(row['LONGITUDE'])
            if float(distance(location, tuple)) < float(dist):
                dist = float(distance(location, tuple))
                uni = row['INSTNM']


    return float(dist), uni
    
