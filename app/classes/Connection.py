from typing import Type
import psycopg2 as pg2

class Database_connection:
    def __init__(
        self,
        host: str,
        database: str,
        user: str,
        password: str,
        port: str
    ) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    
    def __connect(self) -> type[pg2.connect]:
        conn = pg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return conn