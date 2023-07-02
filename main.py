from utils import get_data_vacancies, get_employers_data
from db_manager import DBManager
import psycopg2


db_manager = DBManager(host="localhost", database="hh", user="postgres", password="9184")

# Подключение к базе данных
db_manager.connect()


# Вывод результатов
#db_manager.get_companies_and_vacancies_count()
#db_manager.get_all_vacancies()
#db_manager.get_avg_salary()
#db_manager.get_vacancies_with_higher_salary()
db_manager.get_vacancies_with_keyword("Python")

# Закрытие соединения с базой данных
db_manager.disconnect()
















