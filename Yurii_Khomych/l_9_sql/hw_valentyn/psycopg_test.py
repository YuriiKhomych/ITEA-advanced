from contextlib import closing
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


#
# conn = psycopg2.connect(
#    dbname='postgres',
#    user='test_ps_test',
#    password='test',
#    host='localhost',
# )
# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = conn.cursor()
# cursor.execute('create database test_DB_for_practice')

# conn.autocommit = True
# cursor = conn.cursor()
# cursor.execute("""drop table if exists customers""")
## conn.commit()
## con.rollback()
# cursor.execute("""
# create table customers
# (
#    id            serial primary key,
#    customer_name varchar,
#    contact_name  varchar,
#    address       varchar,
#    city          varchar,
#    postal_code   varchar,
#    country       varchar
# )""")
#
# customers = (
# ('Alfreds Futterkiste ', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany'),
# ('Ana Trujillo Emparedados', ' Ana Trujillo', 'Avda. de la Constitución 2222', 'México', 'D.F. 05021', 'Mexico'),
# ('Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312', 'México', 'D.F. 05023', 'Mexico')
# )
#
#
# cursor.execute("""select * from customers""")
# for row in cursor:
#    print(row)
# with conn:
#    query = """insert into customers (customer_name,
#                           contact_name,
#                           address,
#                           city,
#                           postal_code,
#                           country)
#    values (%s, %s, %s, %s, %s, %s)"""
#    cursor.executemany(query, customers)
#    cursor.execute("update customers set city=%s where id=%s", ("Kyiv", 1))
#    cursor.rowcount
#

# cursor.execute("""select * from customers""")
# for row in cursor:
#    print(row)


def create_db(cursor, db_name):
    query = f"create database {db_name}"
    cursor.execute(query)


def create_table_products(cursor, conn):
    cursor.execute("""
    create table products
    (
        productID   serial primary key,
        productName varchar,
        supplierID  varchar,
        categoryID       varchar,
        description          varchar,
        price   varchar
        
    )""")

    products = (
        ('Candy', '1', '1', '100 gramm', '10'),
        ('Candy', '1', '1', '100 gramm', '10'),
        ('Passat', '2', '2', '2l', '1000'),
        ('Chocolate', '1', '1', '300 gramm', '30'),
        ('Audy', '2', '2', 'White', '300'),
        ('Pet Feed', '3', '3', 'Fish', '50'),
    )

    # with conn:
    #   query = """insert into products (productName,
    #                          supplierID,
    #                          categoryID,
    #                          description,
    #                          price)
    #   values (%s, %s, %s, %s, %s)"""
    #   cursor.executemany(query, products)
    #   #cursor.execute("update customers set city=%s where id=%s", ("Kyiv", 1))
    # cursor.rowcount


def create_table_orders(cursor, conn):
    cursor.execute("""
    create table orders
    (
        orederID   serial primary key,
        productID varchar,
        supplierID  varchar,
        customerID       varchar,
        
        qty   varchar

    )""")

    orders = (
        ('1', '1', '1', '10'),
        ('2', '3', '2', '20'),
        ('3', '2', '3', '30'),
        ('4', '4', '3', '3'),
        ('5', '3', '2', '22'),
        ('6', '1', '1', '1'),
        ('4', '2', '2', '1'),
        ('3', '1', '1', '2'),

    )

    with conn:
        query = """insert into orders (productID,
                             supplierID,
                             customerID,
                             qty)
        values (%s, %s, %s, %s)"""
        cursor.executemany(query, orders)


def create_table_suppliers(cursor, conn):
    cursor.execute("""
    create table suppliers
    (
        supplierID   serial primary key,
        name varchar,
        phone  varchar
        

    )""")

    suppliers = (
        ('Sweet World', '10005-555-666'),
        ('Avtoplace', '444-55-3334'),
        ('Animal conner', '4024-55-666'),
        ('Jeans', '23454-22-45'),

    )


def main():
    conn = psycopg2.connect(
        dbname='postgres',
        user='test_ps_test',
        password='test',
        host='localhost',
    )
    cursor = conn.cursor()
    # create_table_suppliers(cursor, conn)
    # create_table_products(cursor, conn)
    # create_table_orders(cursor, conn)

    cursor.execute("""SELECT * FROM customers""")
    for row in cursor:
        print(row)

    cursor.execute("""SELECT * FROM products""")
    for row in cursor:
        print(row)

    cursor.execute("""SELECT * FROM suppliers""")
    for row in cursor:
        print(row)

    cursor.execute("""SELECT qty,customers.contact_name,products.productName FROM orders LEFT JOIN customers ON orders.customerID::varchar = customers.id::varchar
    LEFT JOIN products ON orders.productID::varchar = products.productID::varchar""")
    for row in cursor:
        print(row)


if __name__ == '__main__':
    main()
