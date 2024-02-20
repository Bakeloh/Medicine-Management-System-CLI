from models import User,Comments
from sqlalchemy.orm import Session
from connect import engine

sesion = Session(bind=engine)