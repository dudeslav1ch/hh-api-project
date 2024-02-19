from src.GetApiHh import GetApiHh
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


def user_interaction():
    platforms = ["HeadHunter"]
    hh_api = GetApiHh()

    search_query = input("Введите поисковый запрос: ").title()
    vacancies_getter = hh_api.get_vacancies(search_query)

    while True:
        user_salary = input("Введите минимальную зарплату: ")
        if user_salary.isdigit():
            break
        print("Вводите только цифры")

    json_saver = JSONSaver()
    json_saver.save_vacancies(vacancies_getter)
    file_vacancies = json_saver.read_file()
    json_saver.delete_vacancies()

    vacancies = Vacancy.cast_to_object_list(file_vacancies, int(user_salary))
    sorted_vacancies = sorted(vacancies)

    while True:
        count = input("Введите количество вакансий для вывода в топ: ")
        if count.isdigit():
            break
        print("Вводите только цифры")

    Vacancy.print_vacancies(sorted_vacancies, count)


if __name__ == "__main__":
    user_interaction()
