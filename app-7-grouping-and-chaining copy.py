from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import func

import random

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on
session = Session()  # then we return the actual session object to perform actions

# Group by age  # SELECT age FROM users GROUP BY age;
users = session.query(User.age).group_by(User.age).all()
print(users)
print()

users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(users)
print()

users = session.query(User.name, func.count(User.id)).group_by(User.name).all()
print(users)


# CHAINING
print("\nChaining\n")
# the same as: session.query(User).filter(User.age > 24, User.age < 50).all()
users = session.query(User).filter(User.age > 24).filter(User.age < 50).all()
print(len(users))


# SELECT age, COUNT(id) FROM users WHERE age > 24 AND age < 50 GROUP BY age ORDER BY "age";
users_tuple = (
  session.query(User.age, func.count(User.id))
  .filter(User.age > 24)
  .order_by(User.age)
  .filter(User.age < 50)
  .group_by(User.age)
  .all()
)

for age, count in users_tuple:
  print(f"Age: {age} - {count} users")

print('*'*20)

# Conditional Chaining
print('Conditional Chaining')

only_iron_man = True
group_by_age = True

users = session.query(User)
print(users, "\n") # this will output the `query` set to be used on the db so far

if only_iron_man:
  users = users.filter(User.name == 'Iron man')
  print(users, "\n")

if group_by_age:
  users = users.group_by(User.age)
  print(users, "\n")

users = users.all()

print(users,"\n")

for user in users:
  print(f"User age: {user.age}, name: {user.name}")

