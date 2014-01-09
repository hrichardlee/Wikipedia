# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia
from request_mock_data import mock_data


# mock out _wiki_request
def _wiki_request(**params):
  return mock_data["_wiki_request calls"][tuple(sorted(params.items()))]
wikipedia._wiki_request = _wiki_request

# http://en.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&rvprop=size&titles=Sonic%202%20Beta|Menlo_Park,%20New%20Jersey%7CEuclid|Newton|Albert_Einstein&redirects=&indexpageids
class TestBatch(unittest.TestCase):
	def test_something(self):
		self.assertEqual(
			wikipedia.batchRevSize(["Geode", "Albert_Einstein", "Menlo_Park, New Jersey"]),
			[6718, 106218, 86560])

class TestFollowReplacements(unittest.TestCase):
	def test_one(self):
		r = [{"from": 1, "to": 2}, {"from": 2, "to": 3}, {"from": 7, "to": 8}]
		t = {1: set([10]), 7: set([11])}
		wikipedia._followReplacements(t, r)
		self.assertEqual(
			t,
			{3: set([10]), 8: set([11])})
	def test_two(self):
		r = [{"from": 1, "to": 2}, {"from": 2, "to": 3}, {"from": 7, "to": 8}]
		t = {1: set([10]), 2: set([12]), 7: set([11])}
		wikipedia._followReplacements(t, r)
		self.assertEqual(
			t,
			{3: set([10, 12]), 8: set([11])})