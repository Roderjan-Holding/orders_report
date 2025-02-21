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

        if cursor:
            html_data = cursor.fetchall()

            extracted_html_data = [
                row[3] for row in html_data if row[3] and isinstance(row[3], str)
            ]

            if extracted_html_data:
                return extracted_html_data
            else:
                raise ValueError("No HTML data returned from the database.")
        else:
            raise ValueError("Failed to execute query.")

    def __decode_html(self) -> str:
        html_strings = self.__extract_html()

        decoded_html_list = []

        for string in html_strings:
            decoded_string = html.unescape(string)
            soup = BeautifulSoup(decoded_string, "html.parser")
            decoded_html_list.append(soup.prettify())
        return decoded_html_list
    
    def get_html(self) -> str:
        return self.__decode_html()