import unittest

from fleet import Carrigan


class TestOctoprimeFleet(unittest.TestCase):
    def test_needs_service_true(self):

        integer_list = [1, 1, 1, 1]
        fleet = Carrigan(integer_list)
        self.assertTrue(fleet.needs_service())

    def test_needs_service_false(self):
        integer_list = [1, 1, 1, 0]
        fleet = Carrigan(integer_list)
        self.assertFalse(fleet.needs_service())