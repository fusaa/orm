from sqlalchemy.orm import sessionmaker
from models import User, engine

import random

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on
session = Session()  # then we return the actual session object to perform actions

names = ["Iron man", "Charles Nice", "Monique Hello", "Jane Doe", "John Doe", "Iron Man"]
ages = [20, 22, 44, 33, 23, 43, 50, 41]

for x in range(20):
  user = User(name=random.choice(names), age=random.choice(ages))
  session.add(user)

session.commit()
