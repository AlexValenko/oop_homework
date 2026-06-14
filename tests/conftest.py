import pytest

from src.products import Product, Category

@pytest.fixture
def get_test_product():
    prod_1 = Product(
        name='Product 1',
        description='Some Product 1',
        price= 100.0,
        quantity=10
    )
    return prod_1

@pytest.fixture
def get_test_category():
    return Category(
        name='cat_1',
        description='Something about cat_1',
        products=[Product(name='PC1', description="PC-1", price=10.0, quantity=5),
                  Product(name='PC2', description="PC-2", price=20.0, quantity=5),
                  Product(name='PC3', description="PC-3", price=30.0, quantity=5)]
    )
