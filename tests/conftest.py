import pytest

from src.lawngrass import LawnGrass
from src.products import Category, Product
from src.smartphones import Smartphone


@pytest.fixture(autouse=True)
def reset_product_list() -> None:
    Product.prod_list.clear()
    yield


@pytest.fixture
def get_test_product() -> Product:
    prod_1 = Product(name="Product 1", description="Some Product 1", price=100.0, quantity=10)
    return prod_1


@pytest.fixture
def get_product_from_dict() -> Product:
    prod_2 = Product.new_product({"name": "Phone", "description": "some description", "price": 2000, "quantity": 5})
    return prod_2


@pytest.fixture
def get_test_category() -> Category:
    return Category(
        name="cat_1",
        description="Something about cat_1",
        products=[
            Product(name="PC1", description="PC-1", price=10.0, quantity=5),
            Product(name="PC2", description="PC-2", price=20.0, quantity=5),
            Product(name="PC3", description="PC-3", price=30.0, quantity=5),
        ],
    )


@pytest.fixture
def get_one_smartphone():
    """Возвращает объект класса Смартфон, дочернего от Продукты"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def get_one_lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def get_data_from_json() -> list:
    """Данные из файла product.json для тестирования"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
