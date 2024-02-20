from models import Base, User, Comments
from connect import engine


print("CREATING TABLES >>>>")
Base.metadata.create_all(bind=engine)