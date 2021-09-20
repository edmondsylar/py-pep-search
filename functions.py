import datefinder

# function to get the date of birth from the desciption
def get_birth_date(description):
    matches = list(datefinder.find_dates(description))
    if len(matches) > 0:
        date = matches[0]
        return date
    else:
        return ('undefined')