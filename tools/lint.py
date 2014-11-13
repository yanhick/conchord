#!/usr/bin/env python

from sys import stdin
from sys import stdout
from sys import stderr
from parser import parse
import argparse

argParser = argparse.ArgumentParser(description='Check valididty of stdin, line by line until EOF'
            'Output each line to stdout. Output any error to stderr')
argParser.add_argument('--tolerant', help='if true, don\'t exit on first error', action="store_true")
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
