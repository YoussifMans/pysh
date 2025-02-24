import os
import sys

def tokenize(string):
    return string.split()

def parse(tokens):
    command = '' if len(tokens) == 0 else tokens[0]
    
    if len(tokens) > 0:
        tokens.pop()

    match command:
        case 'exit':
            exit()

        case 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')

        case _:
            print(f'"{command}": Bad command or filename')