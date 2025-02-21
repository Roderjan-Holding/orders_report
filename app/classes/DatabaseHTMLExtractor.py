from  bs4 import BeautifulSoup
import html

class DatabaseHTMLExtractor():
    def __init__(
        self,
        queries,
        databaseConnection
    ) -> None:
        self.queries = queries
        self.databaseConnection = databaseConnection
    
    def __extract_html(self) -> str:
        query = self.queries.GET_ALL_FINISHED_ORDERS

        cursor = self.databaseConnection.execute(query)
        html_data = cursor.fetchone()
        
        if html_data:
            return html_data[0]
        else:
            raise ValueError("No HTML data returned from the database.")

    def __decode_html(self) -> str:
        html_string = self.__extract_html()
        decoded_html = html.unescape(html_string)
        soup = BeautifulSoup(decoded_html, "html.parser")
        return soup
    
    def get_html(self) -> str:
        return self.__decode_html()