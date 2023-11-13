import unittest
from src.item import Item


class TestItemMethods(unittest.TestCase):
    def setUp(self):
        self.item = Item("TestItem", 10.0, 3)

    def test_calculate_total_price(self):
        self.assertEqual(self.item.calculate_total_price(), 30.0)

    def test_apply_discount(self):
        self.item.apply_discount(0.9)
        self.assertEqual(self.item.pay_rate, 0.9)


if __name__ == '__main__':
    unittest.main()