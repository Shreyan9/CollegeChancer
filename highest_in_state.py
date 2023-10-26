import csv


def highest_in_state(state):
    """
    Returns the name and cost of the most expensive university in state

    We're using the TUITIONFEE_IN field as cost and INSTNM as the school
    name.

    Be careful on data types on this one. 
    """
    highest = 0
    highestUni = "" 
    csv_file = csv.DictReader(open('university-data.csv'))
    for row in csv_file :
        if row["STABBR"] == state:
            if row['TUITIONFEE_IN'] != "-" and int(row["TUITIONFEE_IN"]) > int(highest):
                highest = row["TUITIONFEE_IN"]
                highestUni = row["INSTNM"]
    return int(highest), highestUni
