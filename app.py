import os
import sys

from functions import *

os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to the Pysh!')

running = True

HOST_NAME = os.uname().nodename
USERNAME = os.environ.get('USER') or os.environ.get('USERNAME')

while running:
    curdir = os.path.basename(os.getcwd())

    command = input(f'[{USERNAME}@{HOST_NAME} {curdir}]$ ')

    parse(tokenize(command))