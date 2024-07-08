from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


db_url = "sqlite:///database_one_to_many.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# There are ways of creating 1-to-many relationships: Map and Non-mapped method

# Non- Mapped Method

class BaseModel(Base):
  __abstract__ = True  # so other classes can inherit from this
  __allow_unmapped__ = True  # needs this for this method

  id = Column(Integer, primary_key=True)

class Address(BaseModel):
  __tablename__ = "addresses"

  city     = Column(String)
  state    = Column(String)
  zip_code = Column(Integer)
  # street   = Column(String)

  user_id  = Column(ForeignKey("users.id"))  # This will be our foreign key making the relationship
  user     = relationship('User')#, back_populates="addresses")

  def __repr__(self):  # so we make it easier to show data from the class
    return f"<Address(id={self.id}, city='{self.city}')>"

class User(BaseModel):
  __tablename__ = "users"

  name = Column(String)
  age  = Column(Integer)

  # So we want to create a relationship to tell db that users can have more than one address:
  addresses = relationship(Address)  # Essentially a user can have a 'list of addresses'
  # If the Address is an import form another file you can prevent errors by using quotes:
  # addresses = relationship("Address")

  def __repr__(self):
    return f"<Address(id={self.id}, age='{self.age}')>"


Base.metadata.create_all(engine)  # creates db and all the tables
