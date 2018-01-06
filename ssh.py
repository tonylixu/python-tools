import subprocess
import sys

HOST = "www.example.com"
# Ports are hendled in ~/.ssh/config since we use OpenSSH
COMMAND = "uname -a"