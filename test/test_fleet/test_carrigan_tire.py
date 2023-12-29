import sys
sys.path.append('/Users/julia/Desktop/forage-lyft')

import unittest

from fleet import Carrigan


class TestCarriganFleet(unittest.TestCase):
    def test_needs_service_true(self):

        integer_list = [0, 0, 0.9, 0]
        fleet = Carrigan(integer_list)
        self.assertTrue(fleet.needs_service())

    def test_needs_service_false(self):
        integer_list = [0, 0, 0.8, 0]
        fleet = Carrigan(integer_list)
        self.assertFalse(fleet.needs_service())