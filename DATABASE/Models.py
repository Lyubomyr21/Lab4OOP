from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://postgres:12341234@localhost/internet_store", echo = True)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Customer (Base):
    __tablename__ = "customer"

    customerId = Column('customer_id', Integer, primary_key = True)
    customername = Column('customername', String)
    firstName = Column('firstname', String)
    lastName = Column('lastname', String)
    email = Column('email', String, unique = True)
    password = Column('password', String)
    phone = Column('phone', String)

class Goods (Base):
    __tablename__ = "goods"

    goodsId = Column('goods_id', Integer, primary_key = True)
    name = Column('name', String)
    price = Column('price', Integer)
    status = Column('status', Integer)