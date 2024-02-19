# Парсинг вакансий HeadHunter'а
Выводит информацию о вакансиях HH по запросу пользователя

## **Структура проекта:**

### **data:**
* [vacancy.json](data/vacancy.json) - файл, в который отправляются вакансии

### **src:** 

* [GetApiHh.py](src/GetApiHh.py) - класс для работы с API HH'а
* [JSONSaver.py](src/JSONSaver.py) - класс для обработки JSON-файлов
* [Vacancy.py](src/Vacancy.py) - класс вакансии

### **tests:** 
* [test_vacancy](tests/test_vacancy.py)
* [test_GetApiHh](tests/test_GetApiHh.py)
* [test_JSONSaver](tests/test_JSONSaver.py)

### root:
* [config](config.py)
* [main](main.py) - взаимодействие с пользователем
* [pyproject.toml](pyproject.toml)
