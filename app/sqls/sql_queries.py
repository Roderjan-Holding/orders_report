GET_ALL_FINISHED_ORDERS = """
SELECT 
	content 
FROM glpi_tickets 
	WHERE name LIKE '%Solicitação de Compras -%'
	AND status = 5;
"""

GET_ALL_FINISHED_MAINTENCE_ORDERS = """
SELECT 
	content 
FROM glpi_tickets 
	WHERE name LIKE '%Solicitação de Compras de Manutenção -%'
	AND status = 5;
"""