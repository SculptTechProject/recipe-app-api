"""
sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
      def test_add_num(self):
            res = calc.add(5, 6)
            self.assertEqual(res, 11)

      def test_sub_num(self):
            res = calc.sub(15, 5)
            self.assertEqual(res, 10)
