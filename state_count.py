import csv


def state_count(state):
    """
    Returns the number of times a college or university in state is found.

    You're going to want to use the STABBR field and can assume that it's
    case sensitive and will always be the 2 character abbreviation for a
    state
    """
    
    csv_file = csv.DictReader(open('university-data.csv'))
    count = 0
    for row in csv_file:
        if row["STABBR"] == str(state) : 
            count = count+1
    # Do something with the data...

    return count
