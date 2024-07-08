from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on

session = Session()  # then we return the actual session object to perform actions

users = session.query(User).all()  # we specify the class 'of the table' we want to query
user = users[0]

print(user)  # returns object

print(user.id)
print(user.name)
print(user.age)

# user = session.query(User).filter_by(id=2).all()
# user = session.query(User).filter_by(age=43).one_or_none()
user = session.query(User).filter_by(age=43).first()
print(f"\n{user.id} {user.name}  {user.age}")

# user.name = "Iron Man"  # we can change the name


print(f"\n{user.id} {user.name}  {user.age}")

# Now commit the changes, so it records in the db:
# session.commit()

# We can also do delete
session.delete(user)
session.commit()

