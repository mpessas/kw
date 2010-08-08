# -*- coding: utf-8 -*-

"""Exception class for the kw application."""


class EntryNotSpecifiedError(Exception):
    """Exception for when user has not specified
    an entry in the command line."""
    pass


class InvalidTaskError(Exception):
    """Exception for when a user has specified an invalid task."""
    pass


class ValueNotSpecifiedError(Exception):
    """Exception for when a user has not specified a value to be
    saved in kwallet."""
    pass
