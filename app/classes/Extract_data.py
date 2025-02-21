from app.config.config import DatabaseManager
from  bs4 import BeautifulSoup
import html

class ExtractData():
    def __init__(
        self,
        queries,
        databaseConnection: DatabaseManager
    ) -> None:
        self.queries = queries
        self.databaseConnection = databaseConnection
    
    def __get_html(self) -> str:
        pass

    def __decode_html(self) -> str:
        html_string = self.__get_html()
        decoded_html = html.unescape(html_string)
        soup = BeautifulSoup(decoded_html, "html_parser")
        return soup