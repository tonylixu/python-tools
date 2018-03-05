"""
A dates class to parse and represent local calendar.abs
"""
import time
import calendar

from time import localtime, struct_time
from datetime import datetime, date, timedelta

# Define default date format
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
# Define default first day of week
DEFAULT_WEEK_START_DAY = 1
# Define default number of workdays per week
DEFAULT_WORKDAYS_PER_WEEK = 5

class Day():
    """
    Extension of datetime.date object supporting iteration
    and some basic operations
    """
    def __init__(self, value=None, input_format=None):

        if value is None:
            self.value = datetime.now().date()
        # If value is a Day obj
        elif isinstance(value, Day):
            self.value = value.value
        # If value is a date obj
        elif isinstance(value, date):
            self.value = value
        # If value is a datetime obj
        elif isinstance(value, datetime):
            self.value = value.date()
        # If value is an empty str
        elif isinstance(value, str) and input_format is None and value == '':
            self.value = datetime.now().date()
        else:
            input_format = input_format is not None and input_format or DEFAULT_DATE_FORMAT
            try:
                # Return a datetime obj corresponding to value, parsed according to format
                # datetime.strptime("00-Nov-28", "%y-%b-%d").date() will print
                # 2000-11-28
                self.value = datetime.strptime(str(value), input_format).date()
            except ValueError:
                try:
                    self.value = date(*time.localtime(int(value))[:3])
                except ValueError:
                    raise 'Error parsing date: {0}'.format(value)

    def __getattr__(self, attr):
        if attr == 'weekday':
            return self.value.isoweekday()
        return getattr(self.value, attr)

    def __str__(self):
        return self.value.strftime(DEFAULT_DATE_FORMAT)

    # value is a date obj
    def strftime(self, value):
        return self.value.strftime(value)

    def __repr__(self):
        return self.__str__()

    # Convert to a long integer
    def __long__(self):
        return long(self.value.strftime('%s'))

    def __eq__(self, value):
        return long(self) == long(value)

    def __ne__(self, value):
        return long(self) != long(value)

    def __gt__(self, value):
        return long(self) > long(value)

    def __lt__(self, value):
        return long(self) < long(value)
    
    def __le__(self, value):
        return long(self) <= long(value)

    def __ge__(self, value):
        return long(self) >= long(value)
