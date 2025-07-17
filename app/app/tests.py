"""Sample test module."""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests for calc helper."""

    def test_add_num(self):
        """Test that add returns correct result."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_num(self):
        """Test that sub returns correct result."""
        res = calc.sub(15, 5)
        self.assertEqual(res, 10)
