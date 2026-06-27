from typing import Any
from src.base_product import BaseProduct


class Product(BaseProduct):
    """Класс описывает продукты магазина с их ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int
    prod_list: list

    # Список для хранения всех инициализированных товаров
    prod_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляров класса Product - все атрибуты задаются при инициализации"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.prod_list.append(self)

    def __str__(self):
        """Выводит строковое отображение экземпляра класса в виде
        <Название продукта>, <Цена> руб. Остаток: <Количество> шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """При сложении экземпляров класса Product или дочерних выдает полную стоимость товаров на складе
        (стоимость * количество товара 1) + (стоимость * количество товара 2)
        Не позволяет складывать объекты разных классов, в т.ч. родственных"""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только экземпляры одного класса")
        if self.__price > 0 and self.quantity > 0 and other.__price > 0 and other.quantity > 0:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            return 0

    @classmethod
    def new_product(cls, prod_dict: dict[str, Any]) -> "Product":
        """Метод принимает на вход словарь, в котором ключи соответствуют атрибутам экземпляра класса.
        Создает экземпляр класса. Выполняет проверку имеются ли экземпляры с совпадающим полем name.
        Если продукт с таким именем существует, то в существующем экземпляре добавляется количество товаров
        и актуализируется цена (берется наибольшая). Если продукта с таким именем нет,
        то создается новый экземпляр класса (Продукт)"""

        name = prod_dict.get("name")
        description = prod_dict.get("description")
        price = prod_dict.get("price")
        quantity = prod_dict.get("quantity")

        for prod in cls.prod_list:
            if prod.name == name:
                prod.quantity += quantity
                if price > prod.price:
                    prod.price = price
                return prod

        new_prod = cls(name=name, description=description, price=price, quantity=quantity)

        return new_prod

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута price. Возвращает стоимость товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута price. Реализует проверку: в случае если цена равна или ниже нуля,
        выводите предупреждение в консоль, не изменяя цену товара. В случае если цена товара понижается,
        запрашивается подтверждение пользователя вручную через ввод:
        y (yes) или любой непустой ввод (no) для согласия понизить цену или для отмены действия соответственно."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            print("Вы уверены, что хотите снизить цену?")
            user_verifications = input('Да - введите "y", нет - любой непустой ввод \n').strip().lower()
            if user_verifications == "y":
                self.__price = new_price
            else:
                print("Цена не была изменена")
        else:
            self.__price = new_price


class Category:
    """Класс описывает категории товаров. Атрибуты класса Category считают количество категорий и количество товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляров класса Category - атрибуты экземпляра задаются при инициализации.
        Атрибуты класса: количество категорий и количество товаров обновляются при новой инициализации"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Вычисляет общее количество товаров в категории, возвращает результат в виде строки
        <Название категории>, количество продуктов: <количество> шт."""
        product_list = self.__products
        total_products_count = 0
        for product in product_list:
            if product.quantity <= 0:
                continue
            if isinstance(product.quantity, int):
                total_products_count += product.quantity
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию, принимает на вход объект класса
        Product и записывает его в приватный атрибут списка товаров"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только товары класса Product и дочерних")

    @property
    def products(self) -> str:
        """Геттер для атрибута products, возвращает список товаров в виде строк в формате:
        <Название продукта>, <Цена> руб. Остаток: <Количество> шт."""
        result = ""
        for prod in self.__products:
            result += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return result

    @property
    def products_in_list(self) -> list[Product]:
        """Геттер для атрибута products, возвращает список товаров в виде объектов класса Product"""
        return self.__products


class IterProducts:
    """Класс позволяет перебирать товары одной категории, например в цикле for.
    Принимает на вход объект класса категории и производит итерацию по товарам, которые хранятся в данной категории"""

    def __init__(self, category):
        """Инициализация объекта класса IterProducts на входе объект - class Category"""
        if not isinstance(category, Category):
            raise ValueError("Экземпляр класса IterProducts может принимать только объект класса Category")
        self.category_obj = category
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        products = self.category_obj.products_in_list
        if self._index >= len(products):
            raise StopIteration
        current_product = products[self._index]
        self._index += 1
        return current_product
