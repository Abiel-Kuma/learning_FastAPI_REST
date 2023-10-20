from sqlalchemy import Table, Column
from database import conn_db
from sqlalchemy.sql.sqltypes import Integer, String

engine = conn_db.engine
meta = conn_db.meta

users = Table("user", meta,
        Column("id", Integer),
        Column("name", String(255)), # nullable =False),
        Column("email", String(255)), # nullable= False),
        Column("password", String(255))
    )

meta.create_all(engine)