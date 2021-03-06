"""
Utility functions for python in unix shell.
"""
import sys
import os
import time
import signal
import socket
import argparse
import threading
import unicodedata

from systematic.classes import check_output, CalledProcessError
from subprocess import Popen, PIPE