# -*- coding: utf-8 -*-

"""This module provides classes for the tasks available to use kwallet."""

import pykwallet
from kwerrors import ValueNotSpecifiedError

TASKS = ['get', 'set']
AVAIL_TASKS = '[' + ', '.join(TASKS) + ']'


class KwTask(object):
    """Base class for the available tasks."""

    def __call__(self, folder, entry, key, value=None):
        self.kw.open()
        self.kw.set_folder(folder)
        self.entry = entry
        self.key = key
        self.value = value
        res = self.call()
        self.kw.close()
        return res

    def call(self):
        """Abstract function to actuall execute the task.

        Override this to provide a new task.
        Returns:
            the result or None for error."""
        pass

    def open_wallet(self, wallet):
        """Open the specified wallet."""
        self.wallet = wallet
        app_name = u'kw'
        self.kw = pykwallet.KWallet(app_name, wallet=self.wallet)


class GetKwTask(KwTask):
    """Class to get values from KWallet."""

    def call(self):
        return self.kw.get(self.entry, self.key)


class SetKwTask(KwTask):
    """Class to set values to KWallet."""

    def call(self):
        if not self.value:
            raise ValueNotSpecifiedError(u'No value has been specified.')
        return self.kw.set(self.entry, self.value, self.key)


def get_kwtask(task):
    """Return the correct object for the specified task."""
    task_classes = {TASKS[0]: GetKwTask,
                   TASKS[1]: SetKwTask}
    return task in task_classes and task_classes[task]()
