from __future__ import print_function

import subprocess
import sys

HOST = sys.argv[1]
USER = sys.argv[2]
# Ports are hendled in ~/.ssh/config since we use OpenSSH
COMMAND = "uname -a"

ssh = subprocess.Popen(["ssh", "{}@{}".format(USER, HOST), COMMAND],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print("ERROR: {}".format(error), file=sys.stderr)
else:
    print(result)
