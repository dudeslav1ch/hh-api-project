import json
import requests

from abc import ABC, abstractmethod


class AbstractGetApiHh(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class GetApiHh(AbstractGetApiHh):
    """
    Получает информацию о вакансиях
    """
    def __init__(self):
        self.all_vacancies = []

    def get_vacancies(self, keyword):
        key_response = {'text': f'NAME:{keyword}', 'area': 113, 'per_page': 100}
        url_get = "https://api.hh.ru/vacancies"
        response = requests.get(url_get, key_response)
        self.all_vacancies = json.loads(response.text)['items']
        return self.all_vacancies
