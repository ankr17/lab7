# create_tables.py
import psycopg2

# Database connection
connection = psycopg2.connect(
    host="localhost",
    database="supply_department",
    user="user",
    password="password",
    port=5432
)

cursor = connection.cursor()

# Creating tables
cursor.execute("""
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone CHAR(10) CHECK (phone ~ '^\d{10}$'),
    account_number VARCHAR(20)
);

CREATE TABLE Materials (
    material_id SERIAL PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Deliveries (
    delivery_id SERIAL PRIMARY KEY,
    delivery_date DATE NOT NULL,
    supplier_id INTEGER REFERENCES Suppliers(supplier_id),
    material_id INTEGER REFERENCES Materials(material_id),
    delivery_days INTEGER CHECK (delivery_days BETWEEN 1 AND 7),
    quantity INTEGER NOT NULL
);
""")
connection.commit()
cursor.close()
connection.close()
