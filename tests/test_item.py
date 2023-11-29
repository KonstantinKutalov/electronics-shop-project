import unittest
from src.item import Item
from src.phone import Phone


class TestItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Item.instantiate_from_csv()

    def setUp(self):
        Item.all = []

    def test_set_name(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(item.name, 'Smartphone')

        item.name = 'SuperSmart'
        self.assertEqual(item.name, 'SuperSmart')

    def test_calculate_total_price(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(item.calculate_total_price(), 5000)

    def test_string_to_number(self):
        number_string = '10.5'
        number = Item.string_to_number(number_string)
        self.assertEqual(number, 10.5)

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv()
        self.assertEqual(len(Item.all), 10)
        for item in Item.all:
            self.assertIsInstance(item, Item)
            self.assertIsInstance(item.price, float)
            self.assertIsInstance(item.quantity, int)

    def test_repr(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(repr(item), "Item('Smartphone', 1000, 5)")

    def test_str(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(str(item), 'Smartphone')
# Новые

    # Работает
    def test_phone_number_of_sim(self):
        phone = Phone("iPhone 14", 120_000, 5, 2)
        self.assertEqual(phone.number_of_sim, 2)
    # ?

    def test_add_phone_and_item(self):
        phone = Phone("iPhone 14", 120000, 5, 2)
        item = Item("Смартфон", 10000, 20)

        try:
            result = phone + item
        except TypeError as e:
            self.assertIsInstance(e, TypeError)
        else:
            self.fail("Ошибка TypeError не возникла")


if __name__ == '__main__':
    unittest.main()
