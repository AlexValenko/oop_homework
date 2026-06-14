from src.products import Product, Category

def test_product_init(get_test_product):
    """Тестирование корректной инициализации объекта класса Product"""
    assert get_test_product.name == 'Product 1'
    assert get_test_product.description == 'Some Product 1'
    assert get_test_product.price == 100.00
    assert get_test_product.quantity == 10

def test_category_init(get_test_category):
    """Тестирование корректной инициализации объекта класса Category"""
    assert get_test_category.name == 'cat_1'
    assert get_test_category.description == 'Something about cat_1'
    assert len(get_test_category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3

def test_category_add_new_category():
    """Проверка атрибутов класса Category при добавлении новой категории и двух новых продуктов"""
    cat_2 = Category(
        name='cat_2',
        description='Something about cat_2',
        products=[Product(name='PC11', description="PC-11", price=10.0, quantity=5),
                  Product(name='PC22', description="PC-22", price=20.0, quantity=5)]
    )
    assert Category.category_count == 2 # 1 - при вызове фикстуры в предыдущем тесте + 1 из объекта cat_2
    assert Category.product_count == 5 # 3 - при вызове фикстуры в предыдущем тесте + 2 из объекта cat_2

