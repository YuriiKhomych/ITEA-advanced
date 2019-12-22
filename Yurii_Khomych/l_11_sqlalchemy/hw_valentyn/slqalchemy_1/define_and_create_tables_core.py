from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    inspect)
from sqlalchemy_utils import create_database, drop_database, database_exists

user = "test_ps_test"
password = "test"
host = "localhost"
port = "5432"
db_name = "sql_alc2"
db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(db_url, echo=True)

metadata = MetaData()
users = Table(
    'costumers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('address', String),
)
products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('supplier_id', None, ForeignKey('suppliers.id')),
    Column('price', String, nullable=False)
)
suppliers = Table(
    'suppliers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('address', String),
)

orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('costumer_id', None, ForeignKey('costumers.id')),
    Column('supplier_id', None, ForeignKey('suppliers.id')),
    Column('qty', String, nullable=False)
)

#
def recreate_db(db_url):
    if database_exists(url=db_url):
        drop_database(url=db_url)
    create_database(url=db_url)


def create_tables(engine, metadata):
    metadata.create_all(engine)
#
#
def main():

    result = engine.execute('SELECT * FROM "costumers"')
#
    for _r in result:
        print(_r)
    #recreate_db(db_url=db_url)
    #create_tables(engine=engine, metadata=metadata)
    inspector = inspect(engine)

    # Get table information
    print(inspector.get_table_names())


if __name__ == '__main__':
    main()
