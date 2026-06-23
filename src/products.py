class Product:
    """Класс описывает продукты магазина с их ценой и количеством"""

    name: str
    description: str
    price: float
    quantity: int

    # Список для хранения всех инициализированных товаров
    prod_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляров класса Product - все атрибуты задаются при инициализации"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.prod_list.append(self)

    @classmethod
    def new_product(cls, prod_dict):
        """Метод принимает на вход словарь, в котором ключи соответствуют атрибутам экземпляра класса. Создает экземпляр класса.
        Метод выполняет проверку имеются ли экземпляры с совпадающим полем name. Если продукт с таким именем существует, то
        в существующем экземпляре добавляется количество товаров и актуализируется цена (берется наибольшая).
        Если продукта с таким именем нет, то создается новый экземпляр класса (Продукт)"""

        name = prod_dict.get("name")
        description = prod_dict.get("description")
        price = prod_dict.get("price")
        quantity = prod_dict.get("quantity")

        for prod in cls.prod_list:
            if prod.name == name:
                prod.quantity += quantity
                if price > prod.price:
                    prod.price = price
                return prod

        new_prod = cls(name=name, description=description, price=price, quantity=quantity)

        # cls.prod_list.append(new_prod)
        return new_prod

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            print("Вы уверены, что хотите снизить цену?")
            user_verifications = input('Да - введите "y", нет - любой непустой ввод \n').strip().lower()
            if user_verifications == "y":
                self.__price = new_price
            else:
                print("Цена не была изменена")
        else:
            self.__price = new_price





class Category:
    """Класс описывает категории товаров. Атрибуты класса Category считают количество категорий и количество товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляров класса Category - атрибуты экземпляра задаются при инициализации.
        Атрибуты класса: количество категорий и количество товаров обновляются при новой инициализации"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ''
        for prod in self.__products:
            result += f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n'
        return result

    @property
    def products_in_list(self):
        return self.__products


