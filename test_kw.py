#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import kw

class TestKwArgs(unittest.TestCase):
    def test_get_task(self):
        self.assertFalse(kw.run((), ['get']))

    def test_no_args(self):
        self.assertRaises(kw.InvalidTaskError, kw.run, (), [])

    def test_set_task(self):
        self.assertFalse(kw.run((), ['set']))
        
    def test_wrong_task(self):
        self.assertRaises(kw.InvalidTaskError, kw.run, (), ['invalid_task',])


if __name__ == '__main__':
    unittest.main()
