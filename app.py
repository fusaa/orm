from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# sqlite://:memory:
db_url = "sqlite:///database.db"  # /// = relative path, //// = absolute path

engine = create_engine(db_url)

Base = declarative_base()

Base.metadata.create_all(engine)  # creates db and all the tables

