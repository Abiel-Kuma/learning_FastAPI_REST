from sqlalchemy import create_engine

db_url = "sqlite+pysqlite:///database"
engine = create_engine(db_url, echo=True)