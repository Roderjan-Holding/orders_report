from app.classes.DatabaseHTMLExtractor import DatabaseHTMLExtractor
from app.classes.Connection import DatabaseConnection
from app.sqls import sql_queries as queries

app = DatabaseHTMLExtractor(
    queries=queries,
    databaseConnection=DatabaseConnection
)