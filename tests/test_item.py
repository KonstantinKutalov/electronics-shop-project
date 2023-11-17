# -*- coding: utf-8 -*-
import unittest
from src.item import Item


class TestItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Item.instantiate_from_csv()

    def test_set_name(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(item.name, 'Smartphone')

        item.name = 'SuperSmart'
        self.assertEqual(item.name, 'SuperSmart')

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv()
        self.assertEqual(len(Item.all), 10)
        self.assertIsInstance(Item.all[0], Item)
        self.assertAlmostEqual(Item.all[0].price, 100)
        self.assertEqual(Item.all[0].quantity, 1)

    def test_string_to_number(self):
        number_string = '10.5'
        number = Item.string_to_number(number_string)
        self.assertEqual(number, 10.5)


if __name__ == '__main__':
    unittest.main()
