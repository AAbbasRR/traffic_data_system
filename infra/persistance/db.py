from sqlalchemy import create_engine, DDL
from sqlalchemy.orm import sessionmaker
from decouple import config

clickhouse_host = config("CLICKHOUSE_HOST", default="localhost")
clickhouse_user = config("CLICKHOUSE_USER", default="default")
clickhouse_password = config("CLICKHOUSE_PASSWORD", default="")
clickhouse_db = config("CLICKHOUSE_DB", default="default")
conn_str = f'clickhouse://{clickhouse_user}:{clickhouse_password}@{clickhouse_host}/{clickhouse_db}'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

# initialize db
database = config("WORKING_DB", default="default")
create_database_ddl = DDL(f'CREATE DATABASE IF NOT EXISTS {database}')

# Execute the DDL object using the engine
with engine.connect() as conn:
    conn.execute(create_database_ddl)
