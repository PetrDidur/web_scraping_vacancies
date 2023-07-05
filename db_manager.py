import psycopg2

class DBManager:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

        self.conn = psycopg2.connect(
            host="localhost",
            database="hh",
            user="postgres",
            password="9184")

    def create_database(self):
        conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.database}")
        cur.execute(f"CREATE DATABASE {self.database}")

        conn.commit()

        cur.close()
        conn.close

    def create_tables(self):

        conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database="hh"
        )
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE employers (
                    id SERIAL PRIMARY KEY, 
                    name VARCHAR(255) NOT NULL
                )
            """)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE vacancies (
                    name VARCHAR(255) NOT NULL,
                    employer VARCHAR NOT NULL,
                    salary INT,
                    employer_id SERIAL REFERENCES employers(id),
                    url TEXT  
                )
            """)
        conn.commit()

        cur.close()
        conn.close

    def drop_database(self):
        conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.database}")

        cur.close()
        conn.close


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

    def save_employers_to_db(self, data):
        conn = psycopg2.connect(
            host="localhost",
            database="hh",
            user="postgres",
            password="9184")

        with conn.cursor() as cursor:
            for employer in data:
                query = "INSERT INTO employers (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING"
                cursor.execute(query, (employer))

        conn.commit()
        cursor.close()
        conn.close()

    def save_vacancies_to_db(self, data):
        conn = psycopg2.connect(
            host="localhost",
            database="hh",
            user="postgres",
            password="9184")

        with conn.cursor() as cursor:
            for vacancy in data:
                query = "INSERT INTO vacancies (name, employer, salary, employer_id, url) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (vacancy))

        conn.commit()
        cursor.close()
        conn.close()


    def get_all_vacancies(self):
        query = """
        SELECT * from vacancies
        """

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            for name, employer, salary, id, url in results:
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
            for name, employer, salary, id, url in results:
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

