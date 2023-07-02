--получить вакансии и кол-во
query = """
           SELECT employer, COUNT(*) AS vacancies_count
           FROM vacancies
           GROUP BY employer;
           """

 query = """
        SELECT * from vacancies
        """

query = """
        SELECT *
        FROM vacancies
        WHERE salary > %s;
        """

query = """
        SELECT *
        FROM vacancies
        WHERE name ILIKE %s
        """


