#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get and set values to kwallet.
Default action for get is to copy the value to the KDE clipboard."""

import sys
import optparse
from kwtask import AVAIL_TASKS, get_kwtask
from kwerrors import InvalidTaskError, EntryNotSpecifiedError
from pykwallet import EntryNotFoundError


__version__ = '0.1'
ENCODING = 'UTF-8'


def run(options, args):
    """Execute the specified task."""
    if not args:
        msg = u'Task not specified. Available tasks are %s' % AVAIL_TASKS
        raise InvalidTaskError(msg)
    task_name = args.pop(0).decode(ENCODING)
    if not args:
        msg = u'Entry not specified.'
        raise EntryNotSpecifiedError(msg)
    entry_name = args.pop(0).decode(ENCODING)
    value = None
    if args:
        value = args.pop(0).decode(ENCODING)
    task = get_kwtask(task_name)
    task.open_wallet(options.wallet.decode(ENCODING))
    if not task:
        msg = u'%s is not a valid task. Available tasks are %s' % (task_name,
                                                                   AVAIL_TASKS)
        raise InvalidTaskError(msg)
    print task(options.folder.decode(ENCODING),
               entry_name,
               options.key.decode(ENCODING),
               value)


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
        argv = sys.argv
    parser = setup_parser()
    (options, args) = parser.parse_args()
    try:
        run(options, args)
    except EntryNotFoundError, e:
        print u'Specified entry not found.'
        return -1
    except EntryNotSpecifiedError, e:
        print e
        return -1
    except InvalidTaskError, e:
        print e
        return -1
    return 0

if __name__ == '__main__':
    sys.exit(main())
