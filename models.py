from sqlalchemy import Column,String,Integer,ForeignKey,Boolean
from sqlalchemy.orm import Session,relationship
from database import Base




class Customers(Base):
    __tablename__ = "customers"

    name = Column(String)
    emailId = Column(String)
    contactNumber = Column(Integer,primary_key=True)
    insuranceType = Column(String)
    occupation = Column(String)
    status = Column(String)
    age = Column(String)
    clientUserId = Column(Integer,ForeignKey('clients.clientUserId'))


    client = relationship("Client",back_populates='customer')
    

    


class Client(Base):
    __tablename__ = "clients"
    clientUserId = Column(Integer,primary_key=True)
    name = Column(String)
    insuranceType = Column(String)
    companyName = Column(String)
    employeeId = Column(String)
    password = Column(String)
    customer = relationship('Customers',back_populates='client')




