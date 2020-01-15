#!/usr/bin/python3

from termcolor import colored
import math
import argparse

parser = argparse.ArgumentParser(description='Volume of cylinder')
parser.add_argument('-R', '--radius', metavar='', required=True, type=int, help='Radius of cylinder')
parser.add_argument('-H', '--height', metavar='', required=True, type=int, help='Height of cylinder')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='Print verbose')

args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(colored(volume, 'blue'))
    elif args.verbose:
        print(colored('Volume of cylinder with radius %s and height %s is %s' % (args.radius, args.height, volume), 'blue'))
    else:
        print(colored('Volume of cylinder is %s' % volume, 'blue'))
