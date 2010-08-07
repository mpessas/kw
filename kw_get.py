#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse
from kwerrors import InvalidCommandError


__version__ = '0.1'

TASKS = ['get', 'set',]

class ValueNotFoundError(Exception):
    pass


def run(options, args):
    task = args.pop(0)
    if task not in TASKS:
        tasks = '[' + ', '.join(TASKS) + ']' 
        msg = u'%s is not a valid command. Available commands are %s' % (task, tasks)
        raise InvalidCommandError(msg)

def setup_parser():
    """Setup the parser.

    Returns:
        optparse.OptionParser with option configured.
    """
    usage = u'Usage: %prog cmd_name [options]'
    parser = optparse.OptionParser(usage=usage,
                                   version='%prog ' + __version__)
    parser.add_option('-f', '--f', dest='folder', default=u'Passwords',
                      help=u'Specify the folder you want to use')
    parser.add_option('-k', '--key', dest='key', default='password',
                      help=u'The key for this entry')
    parser.add_option('-w', '--wallet', dest='wallet', default=u'personal',
                      help=u'Specify the wallet to use')
    return parser

def main(argv=None):
    if argv is None:
        argv=sys.argv
    parser = setup_parser()
    (options, args) = parser.parse_args()
    try:
        run(options, args)
    except InvalidCommandError, e:
        print e
        return -1
    except ValueNotFoundError, e:
        print u'Specified entry not found.'
        return -1
    return 0

if __name__ == '__main__':
    sys.exit(main())
