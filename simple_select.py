from persisting import session
from model import User, Comment
from sqlalchemy import select
from main import session    

# statement = select(User).where(User.username.in_(['Noel', 'Tom']))

# result = session.scalers(statement) 

# for user in result:
#     print(user)

users = session.query(User).all()

for user in users:
    print(user)