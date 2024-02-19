from abc import ABC
from src.JSONSaver import AbstractJsonSaver, JSONSaver
import pytest


@pytest.fixture
def fixture_class_list():
    json_saver = JSONSaver()
    json_saver.save_vacancies([{'name': 'Java'}])
    return json_saver


def test_issubclass():
    assert issubclass(AbstractJsonSaver, ABC)
    assert issubclass(JSONSaver, AbstractJsonSaver)


def test_delete_vacancy(fixture_class_list):
    assert fixture_class_list.read_file() == [{'name': 'Java'}]

    fixture_class_list.delete_vacancy('Java')
    assert fixture_class_list.read_file() == []

    assert fixture_class_list.delete_vacancies() != []
