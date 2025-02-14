from bs4 import BeautifulSoup
import html


html_string = """
&#60;div&#62;&#60;h1&#62;Dados do formulário&#60;/h1&#62;&#60;h2&#62;UNIDADE SOLICITANTE&#60;/h2&#62;&#60;div&#62;&#60;b&#62;1) Setor Solicitante : &#60;/b&#62;Group &#38;#62; RODERJAN ACCOUNT &#38;#62; Dpto Fiscal&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;SETOR DESTINO&#60;/h2&#62;&#60;div&#62;&#60;b&#62;2) Setor Destino : &#60;/b&#62;Compras&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;TIPO DE REQUISIÇÃO&#60;/h2&#62;&#60;div&#62;&#60;b&#62;3) Tipo de Requisição : &#60;/b&#62;Compras de Manutenção&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;CLASSIFICAÇÃO CONTÁBIL&#60;/h2&#62;&#60;div&#62;&#60;b&#62;4) C. Contábil : &#60;/b&#62;&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;DESCRITIVO DA REQUISIÇÃO&#60;/h2&#62;&#60;div&#62;&#60;b&#62;5) Descritivo Requisição : &#60;/b&#62;&#60;table style="border-collapse: collapse; width: 100.67%; height: 270.234px;" border="1"&#62;&#60;colgroup&#62;&#60;col style="width: 11.6128%;"&#62;&#60;col style="width: 10.0237%;"&#62;&#60;col style="width: 7.70112%;"&#62;&#60;col style="width: 10.5126%;"&#62;&#60;col style="width: 10.5126%;"&#62;&#60;col style="width: 10.8794%;"&#62;&#60;col style="width: 15.5245%;"&#62;&#60;col style="width: 7.95513%;"&#62;&#60;col style="width: 15.2705%;"&#62;&#60;/colgroup&#62;
&#60;tbody&#62;
&#60;tr style="height: 59.2969px;"&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Item&#60;/strong&#62;&#60;/td&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Quantidade&#60;/strong&#62;&#60;/td&#62;
&#60;td style="border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Cl. Contábil&#60;/strong&#62;&#60;/td&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Unidade de  Medida&#60;/strong&#62;&#60;/td&#62;
&#60;td style="border-width: 1px; height: 59.2969px; text-align: center;"&#62;&#60;strong&#62;Valor  Unitário&#60;/strong&#62;&#60;/td&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Valor Total&#60;/strong&#62;&#60;/td&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Especificações técnicas&#60;/strong&#62;&#60;/td&#62;
&#60;td style="height: 59.2969px; border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Fornecedor&#60;/strong&#62;&#60;/td&#62;
&#60;td style="border-width: 1px; text-align: center;"&#62;&#60;strong&#62;Valor Final&#60;/strong&#62;&#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62;Item&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;23&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;5050&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Unidade&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$10&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$100&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Esp&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Fornecedor&#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62;Mais item&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;20&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;4054&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Metro&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$150&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$3000&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Esp&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;Havan&#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;tr style="height: 23.4375px;"&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62;R$&#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td style="height: 23.4375px;"&#62; &#60;/td&#62;
&#60;td&#62; &#60;/td&#62;
&#60;/tr&#62;
&#60;/tbody&#62;
&#60;/table&#62;&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;URGÊNCIA&#60;/h2&#62;&#60;div&#62;&#60;b&#62;6) Urgência : &#60;/b&#62;Muito Baixa&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;CLIENTES PARTICIPANTES&#60;/h2&#62;&#60;div&#62;&#60;b&#62;7) Clientes Participantes : &#60;/b&#62;&#60;/div&#62;&#60;div&#62;&#38;nbsp;&#60;/div&#62;&#60;h2&#62;OBSERVAÇÕES&#60;/h2&#62;&#60;div&#62;&#60;b&#62;8) OBSERVAÇÕES GERAIS : &#60;/b&#62;&#60;/div&#62;&#60;div&#62;&#60;b&#62;9) Anexo : &#60;/b&#62;Nenhum documento anexado&#60;/div&#62;&#60;div&#62;&#60;b&#62;10) EMPRESA PARA FATURAMENTO : &#60;/b&#62;&#60;/div&#62;&#60;/div&#62;"""

def extract_table_by_columns(html_string):
    decoded_html = html.unescape(html_string)  # Decode HTML entities
    soup = BeautifulSoup(decoded_html, "html.parser")  # Parse the decoded HTML
    
    table = soup.find("table")  # Find the table
    if not table:
        return "No table found."

    # Extract headers (th or first row of td)
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    
    # If no <th> found, try using first row as headers
    if not headers:
        first_row = table.find("tr")
        if first_row:
            headers = [td.get_text(strip=True) for td in first_row.find_all("td")]

    # Initialize dictionary with column names
    columns = {header: [] for header in headers}

    # Extract data rows
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        if len(cells) == len(headers):  # Ensure matching columns
            for i, value in enumerate(cells):
                if value and value != "R$":  # Filter out empty values & "R$"
                    columns[headers[i]].append(value)

    return columns  # Return data organized by column

columns = extract_table_by_columns(html_string)

columns_list = list(columns.values()) 


