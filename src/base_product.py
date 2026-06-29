from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс для класса Product (Продукты)"""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        """Метод сложения экземпляров класса"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Метод создания экземпляра класса"""
        pass

    @abstractmethod
    def price(self):
        """Геттер и сеттер для приватного атрибута price. Возвращает или изменяет стоимость товара"""
        pass
