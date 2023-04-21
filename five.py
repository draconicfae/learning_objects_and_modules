#!/usr/bin/env python3

#Level four plus: use an object to do the printing

import argparse

class Printer:
    def __init__(self, string_to_print):
        self.string_to_print = string_to_print
    
    def doprint(self):
        print(self.string_to_print)
        

argparser = argparse.ArgumentParser(prog="three.py")

argparser.add_argument('-p', '--printstring', required=True)

args = argparser.parse_args()

printer = Printer(args.printstring)
printer.doprint()


