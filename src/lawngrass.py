from src.products import Product

class LawnGrass(Product):
    """Отдельный класс от класса Продуктов, описывает газонную траву"""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color:str):
        """Инициализация экземпляра Газонная трава с расширением атрибутов родительского класса"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
