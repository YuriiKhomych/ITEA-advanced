from ex_1_define_and_create_tables_core import (
    suppliers,
    products,
    users,
    orders,
    engine,
)

ins = users.insert()
conn = engine.connect()

# conn.execute(users.insert(), [
#   {'name': 'Vasya', 'address': 'bla bla str'},
#   {'name': 'Kolya', 'address': 'conner street'},
#   {'name': 'Anton', 'address': 'basement'},
#   {'name': 'Emma', 'address': 'street3'},
# ])


# conn.execute(suppliers.insert(), [
#   {'name': 'Vasya Suplier', 'address': 'Suplierbla bla str'},
#   {'name': 'Kolya Suplier', 'address': 'Suplierconner street'},
#   {'name': 'Anton Suplier', 'address': 'Suplierbasement'},
#   {'name': 'Emma Suplier', 'address': 'Suplierstreet3'},
# ])
# conn.execute(products.insert(), [
#   {'name': 'Candy', 'supplier_id': 1, 'price': '10'},
#   {'name': 'CAr', 'supplier_id': 2,'price': '20'},
#   {'name': 'Eggs', 'supplier_id': 2,'price': '30'},
#   {'name': 'Potato', 'supplier_id': 3,'price': '40'},
#    {'name': 'Toy', 'supplier_id': 4,'price': '50'},
# ])

# conn.execute(orders.insert(), [
#   {'customer_id': 1, 'supplier_id': 1, 'qty': '10'},
#   {'customer_id': 2, 'supplier_id': 2,'qty': '20'},
#   {'customer_id': 3, 'supplier_id': 2,'qty': '30'},
#   {'customer_id': 4, 'supplier_id': 3,'qty': '40'},
#   {'customer_id': 1, 'supplier_id': 4,'qty': '50'},
# ])

conn.close()
