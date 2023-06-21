import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE
from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(32), unique=True, nullable=True)
    registration_date = Column(DATE, default=datetime.date.today())
    update_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self):
        return f"<User: {self.user_id}>"
