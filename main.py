from utils import get_data_vacancies, get_employers_data
from db_manager import DBManager
import psycopg2



db_manager = DBManager(host="localhost", database="postgres", user="postgres", password="9184", port="5432")

db_manager.create_database("hh") #создание БД с названием HH
db_manager.create_tables() #создание таблиц

vacancies_data = get_data_vacancies()
employers_data = get_employers_data()

db_manager.save_employers_to_db(employers_data)
db_manager.save_vacancies_to_db(vacancies_data)

db_manager.get_companies_and_vacancies_count()
db_manager.get_avg_salary()
db_manager.get_all_vacancies()
db_manager.get_vacancies_with_higher_salary()
db_manager.get_vacancies_with_keyword("Стажер")






















