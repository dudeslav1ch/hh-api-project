class Vacancy:
    list_vacancies = []

    def __init__(self, name_vacancy, city, salary_from, salary_to, url):
        """
        :param name_vacancy: название вакансии
        :param city: город вакансии
        :param salary_from: минимальная зп
        :param salary_to: максимальная зп
        :param url: ссылка на ваканисю
        """
        self.name_vacancy = name_vacancy
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        Vacancy.list_vacancies.append(self)

    def __repr__(self):
        return (f"\nName of vacancy: {self.name_vacancy}\n"
                f"City: {self.city}\n"
                f"Salary from: {self.salary_from}\n"
                f"Salary to: {self.salary_to}\n"
                f"URL: {self.url}\n")

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, list_vacancy, salary_from):
        """
        Создает CLS из vacancies.json
        :param list_vacancy: json файл
        :param salary_from: минимальная зп, указанная пользователем
        :return: список с данными о вакансии
        """
        for vacancy in list_vacancy:
            name_vacancy = vacancy['name']
            url = vacancy['url']
            city = vacancy['area']['name']

            if vacancy['salary'] is None:
                continue
            elif vacancy['salary']['from'] and vacancy['salary']['to'] is not None:
                if vacancy['salary']['from'] >= salary_from:
                    salary_from = vacancy['salary']['from']
                    salary_to = vacancy['salary']['to']
                    cls(name_vacancy, city, salary_from, salary_to, url)
                else:
                    continue
            else:
                continue
        return cls.list_vacancies

    @staticmethod
    def print_vacancies(vacancies, count):
        """
        Выводит итоговую информацию по вакансиям
        :param vacancies: отсортированные вакансии
        :param count: количество вакансий которые хочет видить пользователь
        """
        for vacancy in vacancies[:int(count)]:
            print(f"\nВакансия: {vacancy.name_vacancy}")
            print(f"Город: {vacancy.city}")
            print(f"Заработанная плата: {vacancy.salary_from} - {vacancy.salary_to}")
            print(f"URL: {vacancy.url}\n")
