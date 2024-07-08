# check model_one_to_many.py
from model_one_to_many import Address, session, User

# Creating users:
user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)

# Creating addresses:
address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(city="Chicago", state="IL", zip_code="60601")

# Associating addresses with users
# The default behaviour of a relationship in SQL Alchemy is a list structure
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

# Now we can actually add users to the session & commit
session.add(user1)
session.add(user2)
# session.commit()

print(f"{user1.addresses = }")
print(f"{user2.addresses = }")
print(f"{address1.user = }")
