"""
List system processes.

User custom flags for ps command to get process output list
"""
import os
import re
import sys

from datetime import datetime, timedelta
from subprocess import Popen, PIPE
from systematic.classes import SortableContainer

TIME_FORMATS = (
    '%a %b %d %H:%M:%S %Y',
    '%a %d %b %H:%M:%S %Y',
)

PS_FIELDS = (
    'lstart',
    'ppid',
    'pid',
    'ruid',
    'rgid',
    'ruser',
    'vsz',
    'rss',
    'state',
    'tdev',
    'time',
    'command',
)

class ProcessError(Exception):
    pass