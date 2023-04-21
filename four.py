#!/usr/bin/env python3

#Level three plus: delegate printing to a function

import argparse

def print_the_string(thestring):
    print(thestring)

argparser = argparse.ArgumentParser(prog="three.py")

argparser.add_argument('-p', '--printstring', required=True)

args = argparser.parse_args()

print_the_string(args.printstring)


