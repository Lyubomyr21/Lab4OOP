from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash

engine = create_engine("postgresql://postgres:12341234@localhost/internet_store", echo = True)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Customer (Base):
    __tablename__ = "customer"

    id = Column('id', Integer, primary_key = True)
    customername = Column('customername', String)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    email = Column('email', String, unique = True)
    password = Column('password', String)
    phone = Column('phone', String)

    def __init__(self, customername, firstname, lastname, email, password, phone):
        self.customername = customername
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone

class Goods (Base):
    __tablename__ = "goods"

    id = Column('id', Integer, primary_key = True)
    name = Column('name', String)
    price = Column('price', Integer)
    status = Column('status', Integer)

class Buy (Base):
    __tablename__ = "buy"
    id = Column('id', Integer, primary_key = True)
    c_id = Column('c_id', Integer)
    g_id = Column('g_id', Integer)
    quantity = Column('quantity', Integer)