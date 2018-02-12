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