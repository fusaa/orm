from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)  # bind tells Session which database it should be making transactions on

session = Session()  # then we return the actual session object to perform actions

user = User(name='John Doe', age = 30)  # Let's create a 'user'
user_2 = User(name='Mathew Pip', age = 21)
user_3 = User(name='Richard Speeded', age = 43)
user_4 = User(name='Richard Speeded', age = 43)

# session.add(user_4)  # After user has been created, we need to add it to session
# session.add_all([user_2, user_3])  # session can receive a list as well

session.commit()  # Then we commit the transaction


