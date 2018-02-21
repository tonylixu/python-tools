"""
Common wrapper classes defintion
"""
import os

# STDOUT: a special value that can be used as stderr argument and
# make standard error goes to the same handler
# check_output: Run command and returns its output
# CalledProcessError: An exception
from subprocess import STDOUT, check_output, CalledProcessError
from systematic.log import Logger, LoggerError

class SortableContainer(object):
    """
    Sortable containers

    Sort objects by comparing attributes specified in tuple
    self.compare_fields

    List of attributes must match for compared objects or
    comparison will fail
    """
    # Define compare fiedls tuple
    compare_fields = ()

    def __cmp_fields__(self, other):
        if self.compare_fields:
            for field in self.compare_fields:
                a = getattr(self, field)
                b = getattr(other, field)
                if a != b:
                    return (a > b) - (a < b)
            
        else:
            raise "compare_fields is empty"

    def __eq__(self, other):
        return self.__cmp_fields__(other) == 0