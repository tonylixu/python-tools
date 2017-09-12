from __future__ import print_function
'''This Python script search for files and list results with file permissions.

Usage:
    $ python file-search.py
    Enter the file pattern to search for:
    test.py

    FILES FOUND FOR PATTERN  test.py:
    test.py
    ================================

    Permissions for file test.py :
    USR     R
    USR     W
    USR     X
    GRP     -
    GRP     -
    GRP     -
    OTH     -
    OTH     -
    OTH     -
'''
import stat, sys, os, string, commands

