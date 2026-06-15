import pytest

from src.products import Category, Product


@pytest.fixture
def get_test_product():
    prod_1 = Product(name="Product 1", description="Some Product 1", price=100.0, quantity=10)
    return prod_1


@pytest.fixture
def get_test_category():
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
def get_data_from_json():
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
