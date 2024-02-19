from abc import ABC, abstractmethod
import json


class AbstractJsonSaver(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_file(self):
        pass


class JSONSaver(AbstractJsonSaver):

    def save_vacancies(self, vacancies):
        with open("../data/vacancies.json", "w", encoding='utf-8') as file:
            file.write(json.dumps(vacancies, indent=2, ensure_ascii=False))

    def read_file(self):
        with open("../data/vacancies.json", encoding='utf-8') as file:
            return json.load(file)

    def delete_vacancy(self, vacancy):
        new_list = []
        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_vacancies(new_list)
