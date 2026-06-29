from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphones import Smartphone


def test_print_mixin_product(capsys) -> None:
    prod_1 = Product(name="Product 1", description="Some Product 1", price=100.0, quantity=10)
    captured = capsys.readouterr()
    assert "Product(Product 1, Some Product 1, 100.0, 10)" in captured.out
    assert prod_1.name == "Product 1"


def test_print_mixin_smartphone(capsys) -> None:
    smart_1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    captured = capsys.readouterr()
    assert "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)" in captured.out
    assert smart_1.name == "Samsung Galaxy S23 Ultra"


def test_print_mixin_lawngrass(capsys) -> None:
    grass_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    captured = capsys.readouterr()
    assert "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)" in captured.out
    assert grass_1.name == "Газонная трава"
