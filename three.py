#!/usr/bin/env python3

#Level two plus: better handling of command line parameters, so that
#if we mess up we're told so for free.

import argparse

argparser = argparse.ArgumentParser(prog="three.py")

argparser.add_argument('-p', '--printstring', required=True)

args = argparser.parse_args()

print(args.printstring)

