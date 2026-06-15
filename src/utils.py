import json
import os
from json import JSONDecodeError

from src.products import Category, Product


def read_json(path_json: str) -> list:
    """Считывает данные из json и преобразует их в объект python"""
    full_path = os.path.abspath(path_json)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return []
    except JSONDecodeError:
        print("Invalid file JSON")
        return []
    return data


def create_objects_from_json(data: list) -> list:
    """Создает объекты классов Product и Category из содержимого json файла"""
    if not data:
        return []
    categories = []
    for category in data:
        products = []
        for prod in category["products"]:
            products.append(Product(**prod))
        category["products"] = products
        categories.append(Category(**category))
    return categories
