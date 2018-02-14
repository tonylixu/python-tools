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

        if lstart_index != -1:
            self.started = self.__parse_date__(' '.join(fields[lstart_index:lstart_index+5]))
            fields = fields[:lstart_index] + fields[lstart_index+5]
            keys.remove('lstart')
        else:
            self.started = None

        for key in keys:
            try:
                if key == 'command':
                    value = ' '.join(fields[keys.index(key):])
                else:
                    value = fields[keys.index(key)]
            except IndexError as e:
                value = None
            
            if key not in ('ruser', 'user', 'time', 'tdev', 'state', 'command'):
                try:
                    value = int(value)
                except ValueError:
                    pass
                    
            setattr(self, key, value)
    
    def __repr__(self):
        return '{0} {1} {2}'.format(self.username, self.pid, self.command)
    
     def __parse_date__(self, value):
        for fmt in TIME_FORMATS:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                pass
        return None