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

sorted_students = sorted(students.items(), key=lambda s:s[1][2])
print(sorted_students)