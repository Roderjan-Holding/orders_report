import sys
import mysql.connector as mariadb

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
    
    def __connect(self) -> mariadb.connection.MySQLConnection:
        try:
            conn = mariadb.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            return conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Database: {e}")
            sys.exit(1)