from database import Base,get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import models
from schemas import CreateClient
from fastapi.responses import Response
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix="/client",
    tags=["client"]
)


@router.get('/getClients')
async def getAllCustomer(db:Session = Depends(get_db)):
    all = db.query(models.Client).all()
    return all

@router.post('/login/{user_id}/{password}')
async def login(user_id:int,password:str,db:Session = Depends(get_db)):
    user = db.query(models.Client).filter(models.Client.clientUserId == user_id).filter(models.Client.password == password).first()
    if not user:
        raise HTTPException(status_code=404)
    return Response(status_code=200)



@router.post("/createClients")
async def createCustomer(client:CreateClient,db:Session = Depends(get_db)):
    new_client = models.Client()
    new_client.clientUserId = client.clientUserId
    new_client.name = client.name
    new_client.insuranceType = client.insuranceType
    new_client.employeeId = client.employeeId
    new_client.companyName = client.companyName
    new_client.password = client.password
    db.add(new_client)
    db.commit()
    return Response(status_code=200)









   