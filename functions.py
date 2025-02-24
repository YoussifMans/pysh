import os
import sys

HOST_NAME = os.uname().nodename
USERNAME = os.environ.get('USER') or os.environ.get('USERNAME')

def tokenize(string):
    return string.split()

def parse(tokens):
    command = '' if len(tokens) == 0 else tokens[0]
    
    if len(tokens) > 0:
        tokens.pop()
    
    args = tokens

    match command:
        case 'exit':
            exit()

        case 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')

        case 'pwd':
            print(os.getcwd())

        case 'whoami':
            print(USERNAME)

        case 'hostname':
            print(HOST_NAME)

        case 'ls':
            print()

        case _:
            print(f'"{command}": Bad command or filename')