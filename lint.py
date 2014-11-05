#!/usr/bin/env python

#Check validity of stdin until EOF and output to stdout.
#Exit with 0 and no message if valid

from sys import stdin
from sys import stdout
from sys import stderr
from parser import parse

#lint one line, output each error to stderr if any
def lint(line, idx):
    (errors, data) = parse(line)
    map(lambda error: stderr.write(error + ' at line: ' + str(idx) + '\n'), errors)

#lint each line until EOF
for idx, line in enumerate(stdin):
    lint(line, idx)
    stdout.write(line)
