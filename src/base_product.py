from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Базовый класс для класса Product (Продукты)"""


    @abstractmethod
    def __init__(self):
        """ Конструктор объекта"""
        pass

    def __str__(self):
        pass

    def __add__(self, other):
        """Метод сложения экземпляров класса"""
        pass

    @classmethod
    def new_product(cls, prod_dict):
        """Метод создания экземпляра класса"""
        pass

    def price(self):
        """Геттер и сеттер для приватного атрибута price. Возвращает или изменяет стоимость товара"""
        pass



