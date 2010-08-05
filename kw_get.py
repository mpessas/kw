#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


__version__ = 0.1

def arg_parser(prog_name):
    parser = argparse.ArgumentParser(
        description=u'A simple application to handle PIM data',
        prog=prog_name
    )
    parser.add_argument(
        u'cmd'
        
    )
    parser.add_argument('--version',
        action='version',
        version='%(prog)s ' + __version__
    )
                        


def main(argv=None):
    if argv is None:
        argv=sys.argv
    parser = arg_parser(argv[0])

if __name__ == '__main__':
    sys.exit(main())
