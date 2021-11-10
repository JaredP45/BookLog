import datetime


def validateDate(date):
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
        return True
    except ValueError:
        print('Incorrect date format, should be MM/DD/YYYY')
        return False
