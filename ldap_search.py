from __future__ import (absolute_import, print_function)
import subprocess

f_name = 'Bob'
l_name = 'Cool'
ldap_server = 'server'

result = subprocess.Popen('ldapsearch -D "username"  -w secret -h {2} -b "basedn" "displayName={1}, {0}"'.format(f_name, l_name, ldap_server), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for l in result.stdout.readlines():
    if "cn: " in l:
        print(l.split(' ')[1])
