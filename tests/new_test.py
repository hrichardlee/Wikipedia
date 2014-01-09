# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia

class TestNew(unittest.TestCase):
	def test_something(self):
		print wikipedia.page('Carl D. Anderson', auto_suggest=False)

	def test_something_else(self):
		print wikipedia.page('Menlo Park, New Jersey', auto_suggest=False)

	def test_something3(self):
		x = wikipedia.page('Cathode Rays', auto_suggest=False)
		print x.pageid
		print x.content.encode('utf-8')