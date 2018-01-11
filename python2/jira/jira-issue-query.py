from __future__ import print_function

from jira import JIRA
import re

options = {
    'server': 'jira-server',
}
jira = JIRA(options, basic_auth=('username', 'password'))

total_defects = jira.search_issues('project in (BSPA, TUT, DA) AND type = Bug AND resolved >= 2017-1-1', maxResults=10000)
counter = 0
for d in total_defects:
    print(d)
    counter = counter + 1
print(counter)
