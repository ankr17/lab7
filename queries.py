# queries.py
import psycopg2
from prettytable import PrettyTable

# Database connection
connection = psycopg2.connect(
    host="localhost",
    database="supply_department",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Helper function to display query results
def display_query(query, headers):
    cursor.execute(query)
    table = PrettyTable(headers)
    for row in cursor.fetchall():
        table.add_row(row)
    print(table)

# Query 1: Deliveries within 3 days, sorted by supplier name
print("Deliveries within 3 days, sorted by supplier name:")
display_query("""
SELECT Suppliers.company_name, Deliveries.*
FROM Deliveries
JOIN Suppliers ON Deliveries.supplier_id = Suppliers.supplier_id
WHERE Deliveries.delivery_days <= 3
ORDER BY Suppliers.company_name;
""", ["Company Name", "Delivery ID", "Date", "Supplier ID", "Material ID", "Delivery Days", "Quantity"])

# Query 2: Sum to be paid for each delivery
print("\nSum to be paid for each delivery:")
display_query("""
SELECT delivery_id, (quantity * Materials.price) AS total_cost
FROM Deliveries
JOIN Materials ON Deliveries.material_id = Materials.material_id;
""", ["Delivery ID", "Total Cost"])

# Query 3: Deliveries of a specific material (parameterized)
material_id = 1  # Example material ID
print(f"\nDeliveries of material ID {material_id}:")
cursor.execute("""
SELECT * FROM Deliveries WHERE material_id = %s;
""", (material_id,))
for row in cursor.fetchall():
    print(row)

# Query 4: Total quantity of each material from each supplier
print("\nTotal quantity of each material from each supplier:")
display_query("""
SELECT Suppliers.company_name, Materials.material_name, SUM(quantity) AS total_quantity
FROM Deliveries
JOIN Suppliers ON Deliveries.supplier_id = Suppliers.supplier_id
JOIN Materials ON Deliveries.material_id = Materials.material_id
GROUP BY Suppliers.company_name, Materials.material_name;
""", ["Company Name", "Material Name", "Total Quantity"])

# Closing the connection
cursor.close()
connection.close()
