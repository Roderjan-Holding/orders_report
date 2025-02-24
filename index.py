from app.classes.DatabaseHTMLExtractor import DatabaseHTMLExtractor
from app.config.config import DatabaseManager
from app.sqls import sql_queries

db_connection = DatabaseManager()

decoded_html = DatabaseHTMLExtractor(
    queries=sql_queries,
    databaseConnection=db_connection
)

decoded_html_list = decoded_html.get_html()

for idx, html_content in enumerate(decoded_html_list, start=1):
    print(f"HTML Content #{idx}:\n{html_content}\n{'-'*50}")