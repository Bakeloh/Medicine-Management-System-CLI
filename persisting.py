from models import User,Comments
from sqlalchemy.orm import Session
from connect import engine
from main inport Session

# session = Session(bind=engine)


user1 = User(
    username = 'Noel',
    email_address = 'noel@gmail.com',
    Comments = [
        comment(text='This is the first comment'),
        comment(text='I do not agree')
        # 'This is the first comment'
    ]
)

john = User(
    username = 'Tom',
    email_address = 'tom@gmail.com',
    Comments = [
        comment(text='Hello There'),
        comment(text='I agree')
        # 'I agree'
    ]
)

suzzan = User(
    username = 'suzzan',
    email_address = 'suzzan@gmail.com'
)

session.add_all([user1, john, suzzan])

# Commit the transaction - saves the users and their comments in the database

session.commit()