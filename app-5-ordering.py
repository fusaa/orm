from sqlalchemy.orm import sessionmaker
from models import User, engine

import random

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on
session = Session()  # then we return the actual session object to perform actions


# Query all users ordered by age - ascending:
users = session.query(User).order_by(User.age).all()

for user in users:
  print(f"{user.id} {user.name}  {user.age}")

# Query all users ordered by age - descending:
users = session.query(User).order_by(User.age.desc()).all()

for user in users:
  print(f"{user.id} {user.name}  {user.age}")
