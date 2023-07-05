from utils import get_data_vacancies, get_employers_data
from db_manager import DBManager
import psycopg2



db_manager = DBManager(host="localhost", database="hh", user="postgres", password="9184", port="5432")
vacancies_data = get_data_vacancies()
employers_data = get_employers_data()


db_manager.get_all_vacancies()















