import pytest

from src.lawngrass import LawnGrass
from src.products import Product


def test_smartphone_init(get_one_lawngrass) -> None:
    """Тестирование корректной инициализации объекта класса LawnGrass"""

    grass1 = get_one_lawngrass
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"
    assert issubclass(LawnGrass, Product)

def test_lawngrass_init_quantity_below_zero() -> None:
    """Тестирование инициализации объекта класса Smartphone c нулевым количеством"""
    with pytest.raises(ValueError) as exc_info:
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 0, "Россия", "7 дней", "Зеленый")
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
