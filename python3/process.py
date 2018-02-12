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

class Process():
    '''
    Process class definition

    To sort these properly, keys must include at least 'pid' and 'ruser' or 'user'
    '''
    def __init__(self, keys, line):
        keys = [x for x in keys]
        lstart_index = keys.index('lstart')
        fields = line.decode('utf-8').split()