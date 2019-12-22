from sqlalchemy import select, text

from ex_1_define_and_create_tables_core import (
    users,
    suppliers,
    orders,
    products,
    engine,
)

conn = engine.connect()

s = select([users])
result = conn.execute(s)

for row in result:
    print(row)

result.close()

s = text(
    "SELECT name, qty "
    "FROM suppliers, orders WHERE orders.supplier_id=suppliers.id"

)
result = conn.execute(s)

for row in result:
    print(row)

conn.close()
