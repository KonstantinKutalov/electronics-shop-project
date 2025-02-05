import csv
import os


class InstantiateCSVError(Exception):
    """
    Исключение для ошибок при обработке CSV-файла.
    """
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # Добавлякм экземпляр в список all

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join(os.path.dirname(__file__), '../src/items.csv')
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                required_columns = {'name', 'price', 'quantity'}
                if not required_columns.issubset(reader.fieldnames):
                    raise InstantiateCSVError("Файл item.csv поврежден")
                for row in reader:
                    __name = row['name'][:10]
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(__name, price, quantity)
                    cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(string):
        """
        Возвращает число из числа-строки.

        :param string: Число в виде строки.
        :return: Число.
        """
        return float(string)

    def __repr__(self):
        """
        Возвращает описание экземплора класса.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое предоставление экземпляра класса .
            """
        return self.name


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
