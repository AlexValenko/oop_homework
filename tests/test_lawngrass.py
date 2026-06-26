from src.products import Product
from src.lawngrass import LawnGrass
import pytest

def test_smartphone_init(get_one_lawngrass) -> None:
    """Тестирование корректной инициализации объекта класса LawnGrass"""

    grass1 = get_one_lawngrass
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price ==  500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"
    assert issubclass(LawnGrass, Product)

