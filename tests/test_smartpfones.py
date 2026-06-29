import pytest

from src.products import Product
from src.smartphones import Smartphone


def test_smartphone_init(get_one_smartphone) -> None:
    """Тестирование корректной инициализации объекта класса Smartphone"""

    smartphone1 = get_one_smartphone
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"
    assert issubclass(Smartphone, Product)


def test_smartphone_init_quantity_below_zero() -> None:
    """Тестирование инициализации объекта класса Smartphone c отрицательным количеством"""
    with pytest.raises(ValueError) as exc_info:
        Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            -5,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_additions_smartphones(get_one_smartphone, get_one_lawngrass) -> None:
    """Тестирование результата сложения экземпляров класса Smartphone (метод __add__)"""
    smartphone1 = get_one_smartphone
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    result = smartphone1 + smartphone2

    assert result == 2580000.0
    # Если складывать экземпляры разных классов
    with pytest.raises(TypeError) as exc_info:
        smartphone1 + get_one_lawngrass
    assert str(exc_info.value) == "Складывать можно только экземпляры одного класса"


def test_additions_products_fail(get_test_product) -> None:
    """Тестирование функции сложения экземпляров класса Product (метод __add__)
    при попытке сложить экземпляры разных классов Product + string"""
    with pytest.raises(TypeError) as exc_info:
        get_test_product + "Some product string"
    assert str(exc_info.value) == "Складывать можно только экземпляры одного класса"


def test_additions_products_fail2(get_test_product, get_one_smartphone) -> None:
    """Тестирование функции сложения экземпляров класса Product (метод __add__)
    при попытке сложить экземпляры разных классов Product + Smartphone"""
    with pytest.raises(TypeError) as exc_info:
        get_test_product + get_one_smartphone
    assert str(exc_info.value) == "Складывать можно только экземпляры одного класса"
