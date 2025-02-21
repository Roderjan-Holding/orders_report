QUERIE = """
SELECT 
	id, name, status, content 
FROM glpi_tickets 
	WHERE name LIKE '%Solicitação de Compras -%'
	AND status = 5;
"""