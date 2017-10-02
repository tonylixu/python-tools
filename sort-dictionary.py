from __future__ import print_function
'''This script sorts a dictionary of lists by value using the
third item in the list.

    Input: A dictionary
    Output: Sorted dictionary

    Exmaple:
    students = {
        'John': ['Grade1', 'Male', 15],
        'Jane': ['Grade2', 'Female', 12],
        'Dave': ['Grade3', 'Male', 13]}
    $ sort-dictionary:students
    { 'Jane': ['A', 12], 'Dave': ['A', 13], 'John': ['A', 15] }
'''

students = {
    'John': ['Grade1', 'Male', 15],
    'Jane': ['Grade2', 'Female', 12],
    'Dave': ['Grade3', 'Male', 13]}

# Staring from Python2.4, both list.sort() and sorted() added a key para
# to specify a function to be called on each list element to making comparisons.
# This tech is fast because the key func is called exactly once.
# https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys
sorted_students = sorted(students.items(), key=lambda s:s[1][2])
print(sorted_students)