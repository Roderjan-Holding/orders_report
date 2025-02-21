from app.classes.DatabaseHTMLExtractor import DatabaseHTMLExtractor
from app.config.config import DatabaseManager
from app.sqls import sql_queries

db_connection = DatabaseManager()

decoded_html = DatabaseHTMLExtractor(
    queries=sql_queries,
    databaseConnection=db_connection
)

print(decoded_html.get_html)