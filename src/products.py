class Product:
    """Класс описывает продукты магазина с их ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляров класса Product - все атрибуты задаются при инициализации"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс описывает категории товаров. Атрибуты класса Category считают количество категорий и количество товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляров класса Category - атрибуты экземпляра задаются при инициализации.
        Атрибуты класса: количество категорий и количество товаров обновляются при новой инициализации"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
