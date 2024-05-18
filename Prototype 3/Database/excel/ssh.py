#This is code to connect to the raspberry pi and run commands

import getpass
from fabric import Connection, Config

password = getpass.getpass("Enter password: ")