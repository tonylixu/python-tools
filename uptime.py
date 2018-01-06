from __future__ import print_function
from fabric import tasks

env.hosts = ['localhost', 'test']
pattern = re.compile(r'up to (\d+) days')