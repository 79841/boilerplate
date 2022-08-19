
from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence


class User(Base):
    __tablename__ = 'user'

    id_seq = Sequence('USER_ID_SEQ', metadata=Base.metadata, minvalue=1001000)
    id = Column(Integer, Sequence('USER_ID_SEQ'), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)

