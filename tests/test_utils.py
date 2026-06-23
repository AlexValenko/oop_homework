import json
from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json


def test_read_json_missing_path() -> None:
    """Тестирование чтения файла JSON при некорректном задании пути (вернется пустой список)"""
    data_json = read_json("missing_path")
    assert data_json == []


def test_read_json_success() -> None:
    """Тест успешного считывания JSON-файла"""
    # Тестовые данные
    test_data = [{"name": "Product 1", "price": 100}, {"name": "Product 2", "price": 200}]
    json_string = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_string)):
        result = read_json("test.json")

    assert result == test_data
    assert len(result) == 2
    assert result[0]["name"] == "Product 1"


def test_read_json_invalid_json() -> None:
    """Тест обработки повреждённого JSON-файла"""
    with patch("builtins.open", mock_open(read_data="невалидный json {]")):
        with patch("json.load", side_effect=json.JSONDecodeError("Invalid JSON", "test.json", 0)):
            result = read_json("corrupted.json")

    assert result == []


def test_create_objects_from_json(get_data_from_json) -> None:
    """Тестирование корректного создания объектов из файла json"""
    category_from_json = create_objects_from_json(get_data_from_json)
    assert category_from_json[0].name == "Смартфоны"
    assert len(category_from_json[0].products_in_list) == 3


def test_create_objects_from_json_not_data() -> None:
    """Тестирование создания объектов из файла json, если чтение файла не сработало
    - файл отсутствует, пуст или поврежден"""
    empty_data_from_json = create_objects_from_json(data=[])
    assert empty_data_from_json == []
