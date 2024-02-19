from abc import ABC

from src.GetApiHh import GetApiHh, AbstractGetApiHh


def test_issubclass():
    assert issubclass(AbstractGetApiHh, ABC)
    assert issubclass(GetApiHh, AbstractGetApiHh)


def test_get_vacancies():
    hh_api = GetApiHh()
    hh_api.get_vacancies("Python")

    assert len(hh_api.all_vacancies) > 0
