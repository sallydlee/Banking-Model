from sqlalchemy import Column, String, Integer, Boolean, Date, create_engine, Float, DateTime, ForeignKey
import xml.etree.ElementTree as et
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


tree = et.parse('db_auth.xml')
root = tree.getroot()
auth_dict = root[0].attrib


class Base(object):
    created_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


Base = declarative_base(cls=Base)
engine = create_engine('mysql+pymysql://' + auth_dict['username'] + ':' + auth_dict['password'] + '@localhost/' +
                       auth_dict['dbname'], echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class EmployeeTable(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    title = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)


class ClientTable(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    street = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    postal = Column(String(255), nullable=False)
    pin = Column(String(4), nullable=False)
    accounts = relationship('AccountTable', back_populates="clients")


class AccountTable(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    account_number = Column(String(9), unique=True, nullable=False)
    balance = Column(Float, default=0)
    client_id = Column(Integer, ForeignKey('clients.id'))
    clients = relationship("ClientTable", back_populates="accounts")
    account_type = Column(String(50), nullable=False)
    monthly_withdrawal_number = Column(Integer, default=0)


ClientTable.accounts = relationship("AccountTable", order_by=AccountTable.id, back_populates="clients")

Base.metadata.create_all(engine)



