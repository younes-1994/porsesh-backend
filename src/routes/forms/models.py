from src.config.database import Base
from sqlalchemy import Column, String, Integer


class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), nullable=True)
    date = Column(String(50), nullable=True)
    questioner = Column(String(50), nullable=True)
    department = Column(String(50), nullable=True)
    name = Column(String(50), nullable=True)
    national_code = Column(String(50), nullable=True)
    mobile = Column(String(50), nullable=True)
    tel = Column(String(50), nullable=True)
    birth_date = Column(String(50), nullable=True)
    q6 = Column(String(50), nullable=True)
    q7 = Column(String(50), nullable=True)
    q8 = Column(String(50), nullable=True)
    q9 = Column(String(50), nullable=True)
    q10 = Column(String(50), nullable=True)