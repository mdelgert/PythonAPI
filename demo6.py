#https://pythonbasics.org/flask-sqlalchemy/
#https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
#https://realpython.com/python-sqlite-sqlalchemy/#example-program
#https://hackersandslackers.com/python-database-management-sqlalchemy/
#https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create a database engine
engine = create_engine('sqlite:///test.db', echo=True)

# create a Session class to interact with the database
Session = sessionmaker(bind=engine)

# create a base class for declarative models
Base = declarative_base()

# define a model for the "users" table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

# create the table in the database
Base.metadata.create_all(engine)

# create a new user and add it to the database
session = Session()
user = User(name='John', email='john@example.com')
session.add(user)
session.commit()

# retrieve all users from the database
users = session.query(User).all()
print(users)

# update a user's email address
user = session.query(User).filter_by(name='John').first()
user.email = 'john.new@example.com'
session.commit()

# delete a user from the database
# user = session.query(User).filter_by(name='John').first()
# session.delete(user)
# session.commit()

# close the session
session.close()
