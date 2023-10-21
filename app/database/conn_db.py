from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite+pysqlite:///database.db")

metadata = MetaData()
conn = engine.connect()