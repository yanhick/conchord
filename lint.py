#!/usr/bin/env python

#Check validity of stdin until EOF and output to stdout.
#Exit with 0 and no message if valid

from sys import stdin
from sys import stdout
from sys import stderr
from parser import parse
import argparse

argParser = argparse.ArgumentParser(description='Lint open chord format. Check validity of stdin')
argParser.add_argument('--tolerant', help='don\'t exit on error', action="store_true")
args = argParser.parse_args()

#wheter to exit on first error
tolerant = args.tolerant

#lint one line, output error to stderr if any
#default to exit on first error but might be set to be tolerant
def lint(line, idx):
    (errors, data) = parse(line)
    for error in errors:
        err = error[1] + ' at line: ' + str(idx) + '\n'
        if not tolerant:
            exit(err)
        else:
            stderr.write(err)

#lint each line until EOF
for idx, line in enumerate(stdin):
    lint(line, idx)
    stdout.write(line)
