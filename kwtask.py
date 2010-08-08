# -*- coding: utf-8 -*-

import pykwallet
from kwerrors import ValueNotSpecifiedError

TASKS = ['get', 'set']
AVAIL_TASKS = '[' + ', '.join(TASKS) + ']'


class KwTask(object):
    def __init__(self, wallet):
        self.wallet = wallet
        app_name = u'kw'
        self.kw = pykwallet.KWallet(app_name, wallet=self.wallet)

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
        pass


class GetKwTask(KwTask):
    def call(self):
        return self.kw.get(self.entry, self.key)


class SetKwTask(KwTask):
    def call(self):
        if not self.value:
            raise ValueNotSpecifiedError(u'No value has been specified.')
        return self.kw.set(self.entry, self.value, self.key)


def get_kwtask(task, wallet):
    taskClasses = {TASKS[0]: GetKwTask,
                   TASKS[1]: SetKwTask}
    return taskClasses.has_key(task) and taskClasses[task](wallet)
