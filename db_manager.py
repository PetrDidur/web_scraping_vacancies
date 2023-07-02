import psycopg2

class DBManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def disconnect(self):
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        query = """
           SELECT employer, COUNT(*) AS vacancies_count
           FROM vacancies
           GROUP BY employer;
           """

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        for company, vacancies_count in results:
            print(f"Company: {company}, Vacancies Count: {vacancies_count}")

    def get_all_vacancies(self):
        query = """
        SELECT * from vacancies
        """

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            for name, employer, id, salary, url in results:
                print(f"Company: {employer}, vacancy: {name}, salary: { salary}, link: {url}")

    def get_avg_salary(self):
        query = """
        SELECT AVG(salary) AS avg_salary
        FROM vacancies 
        WHERE salary IS NOT NULL;
        """

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        print(f" Средняя зарплата: {round(result[0])}")

    def get_vacancies_with_higher_salary(self):
        avg_salary = 62091
        query = """
        SELECT * 
        FROM vacancies 
        WHERE salary > %s;
        """


        with self.conn.cursor() as cursor:
            cursor.execute(query, (avg_salary,))
            results = cursor.fetchall()
            for name, employer, id, salary, url in results:
                print(f"Company: {employer}, vacancy: {name}, salary: {salary}, link: {url}")


    def get_vacancies_with_keyword(self, keyword: str):
        query = """
        SELECT * 
        FROM vacancies
        WHERE name ILIKE %s
        """

        with self.conn.cursor() as cursor:
            cursor.execute(query, ('%' + keyword + '%',))
            results = cursor.fetchall()
            for name, employer, id, salary, url in results:
                print(f"Company: {employer}, vacancy: {name}, salary: {salary}, link: {url}")

