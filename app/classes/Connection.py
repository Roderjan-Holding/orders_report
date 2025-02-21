import mysql.connector as mariadb
import sys

class DatabaseConnection:
    def __init__(
        self,
        host: str,
        database: str,
        user: str,
        password: str,
        port: int
    ) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = self.__connect()
    
    def __connect(self) -> mariadb.connection.MySQLConnection:
        try:
            conn = mariadb.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Database: {e}")
            sys.exit(1)

    def execute(self, query: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor
        except mariadb.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection.is_connected():
            self.connection.close()