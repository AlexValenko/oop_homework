from unittest.mock import patch

import pytest

from src.products import Category, IterProducts, Product


def test_product_init(get_test_product) -> None:
    """Тестирование корректной инициализации объекта класса Product"""
    assert get_test_product.name == "Product 1"
    assert get_test_product.description == "Some Product 1"
    assert get_test_product.price == 100.00
    assert get_test_product.quantity == 10


def test_product_init_quantity_zero() -> None:
    """Тестирование инициализации товара с нулевым или отрицательным количеством"""
    with pytest.raises(ValueError) as e:
        Product(name="Product 3", description="Some Product 3", price=300.0, quantity=0)
    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_string(get_test_product):
    """Тестирование строкового отображения экземпляра класса Product (метод __str__)"""
    assert str(get_test_product) == "Product 1, 100.0 руб. Остаток: 10 шт."


def test_additions_products(get_test_product, get_product_from_dict) -> None:
    """Тестирование результата сложения экземпляров класса Product (метод __add__)"""
    result_1 = get_test_product + get_product_from_dict
    assert result_1 == 11000.0


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


def test_prod_list_count(get_test_product) -> None:
    """Проверка, что атрибут на уровне класса prod_list корректно сохраняет товары
    при инициализации в список, и обновляется при добавлении товаров"""
    assert len(Product.prod_list) == 1
    Product(name="Product 2", description="Some Product 2", price=200.0, quantity=20)
    assert len(Product.prod_list) == 2


def test_product_new_product(get_product_from_dict) -> None:
    """Тестирование возможности создания экземпляра класса через classmethod new_product,
    со словарем на входе."""
    assert get_product_from_dict.name == "Phone"
    # Добавляем еще один продукт, проверяем геттер price
    prod_3 = Product.new_product({"name": "Watch", "description": "description watch", "price": 1000, "quantity": 10})
    assert prod_3.price == 1000
    assert len(Product.prod_list) == 2


def test_product_double_product() -> None:
    """Тестирование логики при совпадении названия продукта"""
    prod_4 = Product.new_product({"name": "Test", "description": "test description", "price": 1000, "quantity": 2})
    assert prod_4.name == "Test"
    assert len(Product.prod_list) == 1
    # Добавляем еще один продукт, название которого совпадает с существующим, цена выше
    Product.new_product({"name": "Test", "description": "test description", "price": 1200, "quantity": 3})
    # Количество товаров не должно измениться, цена обновляется, кол-во суммируется
    assert len(Product.prod_list) == 1
    assert prod_4.price == 1200
    assert prod_4.quantity == 5
    # Добавляем еще один продукт, название которого совпадает с существующим, цена ниже
    Product.new_product({"name": "Test", "description": "test description", "price": 800, "quantity": 4})
    # Количество товаров не должно измениться, цена остается прежней, кол-во суммируется
    assert len(Product.prod_list) == 1
    assert prod_4.price == 1200
    assert prod_4.quantity == 9


def test_product_price_setter_below_zero(get_test_product, capsys) -> None:
    """Проверка логики сеттера при изменении цены продукта на некорректное значение"""
    # Проверяем создание объекта
    prod_1 = get_test_product
    assert prod_1.name == "Product 1"
    assert prod_1.price == 100.0
    prod_1.price = -100.00
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert prod_1.price == 100.0


def test_product_price_setter_upper(get_test_product) -> None:
    """Проверка логики сеттера при изменении цены продукта в бо́льшую сторону"""
    # Проверяем создание объекта
    prod_1 = get_test_product
    assert prod_1.name == "Product 1"
    assert prod_1.price == 100.0
    prod_1.price = 200.0
    assert prod_1.price == 200.0


def test_product_price_setter_lower(get_test_product, capsys) -> None:
    """Проверка логики сеттера при изменении цены продукта в меньшую сторону"""
    # Проверяем создание объекта
    prod_1 = get_test_product
    assert prod_1.name == "Product 1"
    assert prod_1.price == 100.0

    with patch("builtins.input", return_value="y"):
        prod_1.price = 50.0
        assert prod_1.price == 50.0

    with patch("builtins.input", return_value="n"):
        prod_1.price = 10.0
        captured = capsys.readouterr()
        assert prod_1.price == 50.0
        assert "Цена не была изменена" in captured.out


def test_category_init(get_test_category) -> None:
    """Тестирование корректной инициализации объекта класса Category, тестирование геттера products"""
    assert get_test_category.name == "cat_1"
    assert get_test_category.description == "Something about cat_1"
    assert len(get_test_category.products_in_list) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3
    assert (
        get_test_category.products
        == "PC1, 10.0 руб. Остаток: 5 шт.\nPC2, 20.0 руб. Остаток: 5 шт.\nPC3, 30.0 руб. Остаток: 5 шт.\n"
    )


def test_category_string(get_test_category) -> None:
    """Тестирование строкового отображения экземпляра класса Category (метод __str__)"""
    result_1 = str(get_test_category)
    assert result_1 == "cat_1, количество продуктов: 15 шт."
    # Добавляем продукт с количеством товаров 10 штук
    new_product = Product(name="PC555", description="PC-555", price=55.5, quantity=10)
    get_test_category.add_product(new_product)
    result_2 = str(get_test_category)
    assert result_2 == "cat_1, количество продуктов: 25 шт."


def test_category_add_new_category() -> None:
    """Проверка атрибутов класса Category при добавлении новой категории и двух новых продуктов"""
    cat_count_start = Category.category_count
    prod_count_start = Category.product_count
    Category(
        name="cat_2",
        description="Something about cat_2",
        products=[
            Product(name="PC11", description="PC-11", price=10.0, quantity=5),
            Product(name="PC22", description="PC-22", price=20.0, quantity=5),
        ],
    )
    assert Category.category_count == cat_count_start + 1  # добавлена 1 категория
    assert Category.product_count == prod_count_start + 2  # Добавлено 2 продукта


def test_get_average_price_success(get_test_category) -> None:
    """Тестирование метода получения средней цены товаров в категории - успешный"""
    assert get_test_category.average_price() == 20.0
    # Добавим новый продукт для проверки нового результата
    new_product = Product(name="PC4", description="PC-4", price=40, quantity=4)
    get_test_category.add_product(new_product)
    assert get_test_category.average_price() == 25.0

def test_get_average_price_fail(get_test_category) -> None:
    """Тестирование метода получения средней цены товаров в категории - товары отсутствуют"""
    empty_category = Category(name='empty_test', description='something', products=[])
    assert empty_category.average_price() == 0


def test_category_add_product(get_test_category) -> None:
    """Проверка метода (add_product) добавления продуктов в категорию"""
    current_prod_count = Category.product_count

    new_product = Product(name="PC555", description="PC-555", price=55.5, quantity=55)
    get_test_category.add_product(new_product)

    assert Category.product_count == current_prod_count + 1
    assert "PC555" in get_test_category.products


def test_category_add_product_smartphone(get_test_category, get_one_smartphone) -> None:
    """Проверка метода (add_product) добавления продуктов в категорию"""
    current_prod_count = Category.product_count

    get_test_category.add_product(get_one_smartphone)

    assert Category.product_count == current_prod_count + 1
    assert "Samsung Galaxy S23 Ultra" in get_test_category.products


def test_category_add_product_fail(get_test_category) -> None:
    """Проверка метода (add_product) добавления продуктов в категорию в случае,
    если продукт не является объектом текущего или дочернего класса"""
    with pytest.raises(TypeError) as exc_info:
        get_test_category.add_product("Some_product")
    assert str(exc_info.value) == "Можно добавлять только товары класса Product и дочерних"


def test_iter_products_init_success(get_test_category) -> None:
    """Успешная инициализация объекта класса IterProducts"""
    my_iterator = IterProducts(get_test_category)
    assert my_iterator.category_obj.name == "cat_1"
    assert len(my_iterator.category_obj.products_in_list) == 3

    # Тестирование итератора

    result_1 = next(my_iterator)
    assert result_1.name == "PC1"
    result_2 = next(my_iterator)
    assert result_2.description == "PC-2"
    result_3 = next(my_iterator)
    assert result_3.price == 30.0
    with pytest.raises(StopIteration):
        next(my_iterator)


def test_iter_products_init_failed() -> None:
    """Инициализация объекта класса IterProducts с некорректным объектом на входе"""
    with pytest.raises(ValueError) as e:
        IterProducts("Some-string - not Category object")

    assert str(e.value) == "Экземпляр класса IterProducts может принимать только объект класса Category"
