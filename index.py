from app.classes.HTMLExtractor import HTMLExtractor
from app.config.config import DatabaseManager
from app.sqls import sql_queries

db_connection = DatabaseManager()

decoded_html = HTMLExtractor(
    queries=sql_queries,
    databaseConnection=db_connection
)

