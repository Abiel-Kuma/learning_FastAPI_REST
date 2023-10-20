from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite+pysqlite:///database.db")

meta = MetaData()
conn = engine.connect()