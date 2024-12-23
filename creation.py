import oracledb
from sqlalchemy import text,create_engine
import pandas as pd

dms=oracledb.makedsn('orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com','1521',service_name='orcl')
user="deMTIET_venkatdanush"
password="deMTIET_venkatdanush"
engine=create_engine(f'oracle+oracledb://{user}:{password}@{dms}')
conn=engine.connect()
# with conn:
#     conn.execute(text("""create table customers(cust_id number,name varchar2(20),phno number,email varchar2(30))
# """))
#     conn.execute(text("""create table products(product_id number ,product_name varchar2(20),price number,stock_quantity number)
# """))
#     conn.execute(text("""create table stores(store_id number , store_name varchar2(20),loaction
#                       varchar2(30))
# """))
#     Add primary key to customers table
#     conn.execute(text("""
# ALTER TABLE customers
# ADD CONSTRAINT pk_customers PRIMARY KEY (cust_id)
# """))

# # Add primary key to products table
#     conn.execute(text("""
# ALTER TABLE products
# ADD CONSTRAINT pk_products PRIMARY KEY (product_id)
# """))

# # Add primary key to stores table
#     conn.execute(text("""
# ALTER TABLE stores
# ADD CONSTRAINT pk_stores PRIMARY KEY (store_id)
# """))

#     conn.execute(text("""
# CREATE TABLE sales (
#     sale_id NUMBER PRIMARY KEY,
#     cust_id NUMBER,
#     product_id NUMBER,
#     store_id NUMBER,
#     sale_date DATE,
#     quantity NUMBER,
#     total_amount NUMBER,
#     FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
#     FOREIGN KEY (product_id) REFERENCES products(product_id),
#     FOREIGN KEY (store_id) REFERENCES stores(store_id)
# )
# """))

    
    # conn.commit()
insert_query = '''
INSERT INTO customers(cust_id,name,phno,email)
VALUES (:cust_id, :name,:phno, :email)
'''
insert_query1 = '''
INSERT INTO products(product_id,product_name,price,stock_quantity)
VALUES (:product_id, :product_name,:price, :stock_quantity)
'''
insert_query2 = '''
INSERT INTO stores(store_id, store_name,loaction)
VALUES (:store_id, :store_name,:loaction)
'''
insert_query3 = '''
INSERT INTO sales(sale_id, cust_id, product_id, store_id,sale_date,quantity,total_amount)
VALUES (:sale_id, :cust_id,:product_id,:store_id,TO_DATE(:sale_date, 'YYYY-MM-DD'), :quantity,:total_amount)
'''
customers = [
    {'cust_id': 1, 'name': 'Ravi Kumar', 'phno': 9876543210, 'email': 'ravi.kumar@example.com'},
    {'cust_id': 2, 'name': 'Priya Sharma', 'phno': 8765432109, 'email': 'priya.sharma@example.com'},
    {'cust_id': 3, 'name': 'Amit Verma', 'phno': 7654321098, 'email': 'amit.verma@example.com'},
    {'cust_id': 4, 'name': 'Ravi Kumar', 'phno': 9876543210, 'email': 'ravi.kumar@example.com'}
]
products = [
    {'product_id': 1, 'product_name': 'Laptop', 'price': 50000, 'stock_quantity': 10},
    {'product_id': 2, 'product_name': 'Headphones', 'price': 2000, 'stock_quantity': 50},
    {'product_id': 3, 'product_name': 'Smartphone', 'price': 15000, 'stock_quantity': 30},
    {'product_id': 4, 'product_name': 'Laptop', 'price': 50000, 'stock_quantity': 10}
]
stores = [
    {'store_id': 1, 'store_name': 'Tech World', 'loaction': 'Chennai'},
    {'store_id': 2, 'store_name': 'Gadget Hub', 'loaction': 'Bangalore'},
    {'store_id': 3, 'store_name': 'ElectroMart', 'loaction': 'Hyderabad'},
    {'store_id': 4, 'store_name': 'Tech World', 'loaction': 'Chennai'}
]
sales = [
    {'sale_id': 1, 'cust_id': 1, 'product_id': 1, 'store_id': 1, 'sale_date': '2024-06-01', 'quantity': 1, 'total_amount': 50000},
    {'sale_id': 2, 'cust_id': 2, 'product_id': 2, 'store_id': 2, 'sale_date': '2024-06-02', 'quantity': 2, 'total_amount': 4000},
    {'sale_id': 3, 'cust_id': 3, 'product_id': 3, 'store_id': 3, 'sale_date': '2024-06-03', 'quantity': 1, 'total_amount': 15000},
    {'sale_id': 4, 'cust_id': 1, 'product_id': 1, 'store_id': 1, 'sale_date': '2024-06-01', 'quantity': 1, 'total_amount': 50000}
]


with conn:
    for customer in customers:
        conn.execute(text(insert_query),customer)
    for product in products:
        conn.execute(text(insert_query1),product)
    for store in stores:
        conn.execute(text(insert_query2),store)
    for sale in sales:
        conn.execute(text(insert_query3),sale)           
    conn.commit()
    print("succesfully ad")

