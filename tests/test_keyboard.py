import unittest
from src.keyboard import Keyboard


class TestKeyboard(unittest.TestCase):
    def setUp(self):
        self.keyboard = Keyboard('Dark Project KD87A', 9600, 5)

    def test_initial_language(self):
        self.assertEqual(self.keyboard.language, 'EN')  # проверка начального языка

    def test_change_language(self):
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, 'RU')  #  смена языка на RU

        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, 'EN')  # проверка смены языка обратно на EN

    def test_invalid_language_change(self):
        with self.assertRaises(AttributeError):
            self.keyboard.language = 'CH'


if __name__ == '__main__':
    unittest.main()