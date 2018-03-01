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