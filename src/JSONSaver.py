import os
import json

from abc import ABC, abstractmethod
from config import DATA


class AbstractJsonSaver(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_file(self):
        pass


class JSONSaver(AbstractJsonSaver):

    def save_vacancies(self, vacancies):
        """
        Записывает вакансии в файл
        :param vacancies: список вакансий
        """
        with open(DATA, "w", encoding='utf-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def read_file(self):
        """
        Читает вакансии из файла
        :return: объект Python
        """
        with open(DATA, encoding='utf-8') as file:
            return json.load(file)

    def delete_vacancy(self, vacancy):
        """
        Пересоздает файл без указанной vacancy
        :param vacancy: название вакансии
        """
        new_list = []
        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_vacancies(new_list)

    @staticmethod
    def delete_vacancies():
        """
        Удаляет файл с вакансиями
        """
        os.remove(DATA)
