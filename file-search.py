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

# Get search pattern from user input
try:
    pattern = raw_input("Enter the file pattern to search for:\n")
    command_string = "find " + pattern
    command_out = commands.getoutput(command_string)
    find_results = string.split(command_output, "\n")

    print("Files:")
    for f in find_results:
        mode = stat.S_IMODE(os.lstat(f)[stat.ST_MODE])
        print("Permissions for file {0}".format(f))
        for level in 'USR', 'GRP', 'OTH':
            for perm in 'R', 'W', 'X':
                if mode & getattr(stat,"S_I"+perm+level):
                    print('{0} has {1} permission'.format(level, perm))
                else:
                    print('{0} does NOT have {1} permission'.format(level, perm))
except:
    print("There was a problem - check the message above")
