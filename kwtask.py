# -*- coding: utf-8 -*-

import pykwallet

TASKS = ['get', 'set']

class KwTask(object):
    def __init__(self, wallet):
        self.wallet = wallet
        app_name = u'kw'
        self.kw = pykwallet.KWallet(app_name, wallet=self.wallet)

    def __call__(self, folder, entry, key, value):
        self.kw.open()
        self.set_folder(folder)
        self.entry = entry
        self.key = key
        self.value = value
        self.call()
        self.kw.close()

    @abstract
    def call(self):
        pass


class GetKwTask(Task):
    def call(self):
        return self.kw.get(self.entry, self.key)


class SetKwTask(Task):
    def call(self):
        return self.kw.set(self.entry, self.value, self.key)


def get_kwtask(task):
    taskClasses = {TASKS[0]: 'GetTask',
                   TASKS[1]: 'SetTask'}
    return taskClasses.has_key(task) and taskClasses[task]
