import json
import pytest
from config import DATA_TEST
from src.Vacancy import Vacancy


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)


def test_cast_to_object_list(new_file):
    vacancy = Vacancy.cast_to_object_list(new_file, 50000)
    vacancy2 = Vacancy.cast_to_object_list(new_file, 0)
    false_expected = vacancy > vacancy2
    assert false_expected == False
