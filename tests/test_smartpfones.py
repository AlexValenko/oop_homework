from src.products import Product
from src.smartphones import Smartphone
import pytest

def test_smartphone_init(get_one_smartphone) -> None:
    """Тестирование корректной инициализации объекта класса Smartphone"""

    smartphone1 = get_one_smartphone
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price ==  180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"
    assert issubclass(Smartphone, Product)

