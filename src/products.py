from typing import Any


class Product:
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

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию, принимает на вход объект класса
        Product и записывает его в приватный атрибут списка товаров"""
        self.__products.append(product)
        Category.product_count += 1

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
