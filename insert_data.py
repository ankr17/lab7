# insert_data.py
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="supply_department",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Inserting Suppliers data
cursor.execute("""
INSERT INTO Suppliers (company_name, contact_person, phone, account_number)
VALUES
('WoodCo', 'Alice', '1234567890', '123-456-789'),
('MetalWorks', 'Bob', '2345678901', '234-567-890'),
('PaintPlus', 'Charlie', '3456789012', '345-678-901'),
('BuildIt', 'Diana', '4567890123', '456-789-012');
""")

# Inserting Materials data
cursor.execute("""
INSERT INTO Materials (material_name, price)
VALUES
('Wood', 50.0),
('Lacquer', 20.0),
('Steel parts', 100.0);
""")

# Inserting Deliveries data (example)
cursor.execute("""
INSERT INTO Deliveries (delivery_date, supplier_id, material_id, delivery_days, quantity)
VALUES
('2024-11-01', 1, 1, 3, 100),
('2024-11-02', 2, 3, 2, 50),
('2024-11-03', 3, 2, 4, 75),
('2024-11-04', 4, 1, 1, 120);
""")

connection.commit()
cursor.close()
connection.close()
