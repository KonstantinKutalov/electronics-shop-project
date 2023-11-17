from src.item import Item

# Создание экземпляра класса Item
item = Item('Смартфон', 1000.0, 5)

# Проверка длины наименования товара
print(item.name)  # Output: Смартфон

item.name = 'СуперСмартфон'
print(item.name)  # Output: СуперСмарт

# Инициализация экземпляров класса Item из файла src/items.csv
Item.instantiate_from_csv()

# Проверка метода string_to_number()
number_string = '10.5'
number = Item.string_to_number(number_string)
print(number)  # Output: 10.5
