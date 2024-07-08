from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import or_, and_, not_

import random

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on
session = Session()  # then we return the actual session object to perform actions


# Query all users ordered by age - ascending:
users_all = session.query(User).all()

# Query users with age >= 25
users_filtered = session.query(User).filter(User.age >= 25).all()

print("All users: ", len(users_all))
print("Filtered users: ", len(users_filtered))

# Query users with age >= 25 and name= Iron Man
users_filtered = session.query(User).filter(User.age >= 20, User.name == "Iron man").all()

print("All users: ", len(users_all))
print("Filtered users: ", len(users_filtered), "\n")

# FILTER_BY method (doesnt accept comparison > < >= <=) - only single =:
users = session.query(User).filter_by(age=20).all()
for user in users:
  print(f"{user.name} {user.age}")

# WHERE statement:
users = session.query(User).where(User.age >= 25, User.name == "Jane Doe").all()
print('\nWHERE\n')
for user in users:
  print(f"{user.name} {user.age}")


# OR condition:
users = session.query(User).where(or_(User.age >= 25, User.name == "Jane Doe")).all()
print('\nWHERE\n')
for user in users:
  print(f"{user.name} {user.age}")
# we can also use bitwise operator |
users = session.query(User).where((User.age >= 25) | (User.name == "Jane Doe")).all()
print('\nWHERE bitwise OR\n')
for user in users:
  print(f"{user.name} {user.age}")

# AND condition:
users = session.query(User).where(and_(User.age >= 25, User.name == "Jane Doe")).all()
print('\nWHERE AND\n')
for user in users:
  print(f"{user.name} {user.age}")
# bitwise &
users = session.query(User).where((User.age >= 25) & (User.name == "Jane Doe")).all()
print('\nWHERE AND\n')
for user in users:
  print(f"{user.name} {user.age}")

# NOT operator:
users = session.query(User).where(not_(User.name == "Jane Doe")).all()
print('\nWHERE NOT\n')
for user in users:
  print(f"{user.name} {user.age}")

# Multi parameter eg
print("\n Multi")
users = (
  session.query(User).where(
    or_(
      not_(User.name == "Iron Man"),
      and_(
        User.age > 35,
        User.age < 60
      )
    )
  )
)
for user in users:
  print(f"{user.name} {user.age}")
