import psycopg2
from sqlalchemy import create_engine
import os

from airflow.models import Variable


class Database:
    def __init__(self):
        try:
            pg_password = Variable.get("AZURE_PG_PASSWORD")
        except:
            pg_password = os.environ.get("AZURE_PG_PASSWORD")

        db_params = {
            "dbname": "postgres",
            "user": "shadis",
            "password": pg_password,
            "host": "postgre-sql-shad.postgres.database.azure.com",
            "port": "5432",
            "sslmode": "require",
        }

        self.connection = psycopg2.connect(**db_params)
        self.engine = create_engine(
            f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
        )

    def insert(self, insert_query):
        cursor = self.connection.cursor()

        cursor.execute(insert_query)
        self.connection.commit()
        cursor.close()

    def execute(self, query_):
        cursor = self.connection.cursor()

        cursor.execute(query_)
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
        self.engine.dispose()


if __name__ == "__main__":
    db = Database()
    query = "select count(*) from dpe_tertiaire;"
    cur = db.connection.cursor()
    # Execute a query
    cur.execute(query)
    # Retrieve query results
    n = cur.fetchone()
    print("n:", n)

    active_connections = db.engine.pool.status()
    print(f"-- active connections {active_connections}")

    db.close()
