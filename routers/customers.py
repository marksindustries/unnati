from database import Base,get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import models
from schemas import CreateCustomer
from fastapi.responses import Response
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)


@router.get('/getCustomer/{clientId}')
async def getAllCustomer(clientId:int,db:Session = Depends(get_db)):
    all = db.query(models.Customers).filter(models.Customers.clientUserId == clientId).all()
    return all




@router.post("/createCustomer")
async def createCustomer(customer: CreateCustomer,db:Session = Depends(get_db)):

    new_customer = models.Customers()
    new_customer.name = customer.name
    new_customer.age = customer.age
    new_customer.contactNumber = customer.contactNumber
    new_customer.emailId = customer.emailId
    new_customer.insuranceType = customer.insuranceType
    new_customer.occupation = customer.occupation
    new_customer.status = customer.status
    new_customer.clientUserId = customer.clientUserId

    db.add(new_customer)
    db.commit()
    return Response(status_code=200)

@router.put('/updateCustomer/{client_id}/{contactNumber}/{status}')
async def updateStatusOfcustomer(client_id:int,contactNumber:int,status:str,db:Session = Depends(get_db)):
    users = db.query(models.Customers).filter(models.Customers.clientUserId == client_id).filter(models.Customers.contactNumber ==contactNumber).first()
    if not users:
        raise HTTPException(status_code=404)
    
    users.status = status
    db.add(users)
    db.commit()
    return Response(status_code=200)


@router.delete('/deleteCustomer/{client_id}/{customer_number}')
async def deleteCustomer(client_id:int,customer_number:int,db:Session = Depends(get_db)):
    user = db.query(models.Customers).filter(models.Customers.clientUserId == client_id).filter(models.Customers.contactNumber == customer_number).first()
    if not user:
        raise HTTPException(status_code=404)
    
    db.query(models.Customers).filter(models.Customers.clientUserId == client_id).filter(models.Customers.contactNumber == customer_number).delete()
    db.commit()
    return Response(status_code=200)
    






