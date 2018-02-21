"""
Common wrapper classes defintion
"""
import os
import pwd

# STDOUT: a special value that can be used as stderr argument and
# make standard error goes to the same handler
# check_output: Run command and returns its output
# CalledProcessError: An exception
from subprocess import STDOUT, check_output, CalledProcessError
from systematic.log import Logger, LoggerError