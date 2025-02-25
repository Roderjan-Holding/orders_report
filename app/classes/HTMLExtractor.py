from app.classes.DatabaseHTMLExtractor import DatabaseHTMLExtractor
from bs4 import BeautifulSoup
import html

class HTMLExtractor(DatabaseHTMLExtractor):
    def __init__(
        self,
        queries,
        databaseConnection
    ) -> None:
        super().__init__(
            queries,
            databaseConnection
        )

    def __extract_company_billing(self) -> str:
        pass

    def __extract_table_headers(self, table) -> list:
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        if not headers:
            first_row = table.find("tr")
            if first_row:
                headers = [td.get_text(strip=True) for td in first_row.find_all("td")]
        return headers

    def __extract_table_by_columns(self) -> dict:
        columns = {}
        html_data_list = self.get_html()

        for html_data in html_data_list:
            table = html_data.find("table")
            if not table:
                continue

            headers = self.__extract_table_headers(table)
            for header in headers:
                if header not in columns:
                    columns[header] = []

            rows = table.find_all("tr")[1:]
            for row in rows:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if len(cells) == len(headers):
                    for i, value in enumerate(cells):
                        if value and value != "R$":
                            columns[headers[i]].append(value)

        if not columns:
            return {"Error": "No table found in any HTML fragment."}

        return columns

    def __sum_budgeted_values(self):
        table_sums = []
        html_data_list = self.get_html()

        for html_data in html_data_list:
            table = html_data.find("table")
            if not table:
                continue

            headers = self.__extract_table_headers(table)
            rows = table.find_all("tr")[1:]
            table_sum = 0.0
            for row in rows:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if len(cells) == len(headers):
                    for i, value in enumerate(cells):
                        if headers[i] == "Valor Total" and value and value != "R$":
                            table_sum += float(value.replace("R$", "").replace(",", "."))
            table_sums.append(table_sum)

        return table_sums

    def get_company_billing(self) -> str:
        return self.__extract_company_billing()

    def get_table(self) -> dict:
        return self.__extract_table_by_columns()
    
    def get_budgeted_values(self) -> list:
        return self.__sum_budgeted_values()