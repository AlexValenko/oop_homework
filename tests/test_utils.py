from src.utils import create_objects_from_json, read_json


def test_read_json_missing_path() -> None:
    """Тестирование чтения файла JSON при некорректном задании пути (вернется пустой список)"""
    data_json = read_json("missing_path")
    assert data_json == []


def test_create_objects_from_json(get_data_from_json) -> None:
    """Тестирование корректного создания объектов из файла json"""
    category_from_json = create_objects_from_json(get_data_from_json)
    assert category_from_json[0].name == "Смартфоны"
    assert len(category_from_json[0].products) == 3


def test_create_objects_from_json_not_data() -> None:
    """Тестирование создания объектов из файла json, если чтение файла не сработало
    - файл отсутствует, пуст или поврежден"""
    empty_data_from_json = create_objects_from_json(data=[])
    assert empty_data_from_json == []
