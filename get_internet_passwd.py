from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
'''This Python script searches OSX keyChain app and
returns password for given account.

    Example:
        get_keychain_pass('tony@gmail.com', 'imap.gmail.com') retunrs
    tony@gmail.com password.
'''
import re
import subprocess

def main():
    get_keychain_pass('tony@gmail.com', 'imap.gmail.com')

def get_keychain_pass(account=None, server=None):
    '''Search OSX keychain app and return password if found

    Example:
        get_keychain_pass('tony@gmail.com', 'imap.gmail.com') retunrs
    tony@gmail.com password.

    Note:
        This only searches internet password.

    Args:
        account: Internet account
        server: Internet service name

    '''

    params = {
            'security': '/usr/bin/security',
            'command': 'find-internet-password',
            'account': account,
            'server': server,
            'keychain': '/Users/txu/Library/Keychains/login.keychain',
        }
    command = 'sudo {0} -v {1} -g -a {2} -s {3} {4}'.format(
        params['security'], params['command'], params['account'],
        params['server'], params['keychain'])

    try:
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as err:
        print('FAILED: {0}'.format(err))
        raise

    for line in output.splitlines():
        if line.startswith('password: '):
            outtext = line

    password = re.match(r'password: "(.*)"', outtext).group(1)
    print('password is {0}'.format(password))
    return password

if __name__ == '__main__':
    main()
