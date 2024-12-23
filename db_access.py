import oracledb
from sqlalchemy import create_engine, text
import pandas as pd
dms = oracledb.makedsn('orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com', '1521', service_name='orcl')
user = 'deMTIET_venkatdanush'
password = 'deMTIET_venkatdanush'
engine = create_engine(f'oracle+oracledb://{user}:{password}@{dms}')
conn = engine.connect()
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE student_details_dim (
            s_id NUMBER,
            s_name VARCHAR2(30),
            s_dob DATE,
            s_address VARCHAR2(30)
        )
    """))
insert_query = '''
INSERT INTO student_details_dim (s_id, s_name, s_dob, s_address)
VALUES (:s_id, :s_name, TO_DATE(:s_dob, 'YYYY-MM-DD'), :s_address)
'''
students = [
    {'s_id': 1, 's_name': 'Alice', 's_dob': '2000-05-12', 's_address': 'Bangalore'},
    {'s_id': 2, 's_name': 'Bob', 's_dob': '1999-09-23', 's_address': 'Mysore'},
    {'s_id': 3, 's_name': 'Charlie', 's_dob': '2001-03-15', 's_address': 'Hubli'},
    {'s_id': 1, 's_name': 'Alice', 's_dob': '2000-05-12', 's_address': 'Bangalore'}
]
with engine.connect() as conn:
    for student in students:
        conn.execute(text(insert_query),student)
        conn.commit()


print("Records inserted successfully!")






