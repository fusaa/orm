from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# sqlite://:memory:
db_url = "sqlite:///database.db"  # /// = relative path, //// = absolute path

engine = create_engine(db_url)

Base = declarative_base()


class User(Base):  # to create a table we create a class and inherit from base
  __tablename__ = 'users'  # typically the class name is singular and the table name plural

  # Then we add columns:
  id    = Column(Integer, primary_key=True)
  name  = Column(String)
  age   = Column(Integer)

Base.metadata.create_all(engine)  # creates db and all the tables
