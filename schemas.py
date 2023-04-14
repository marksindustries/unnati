from pydantic import BaseModel


class CreateCustomer(BaseModel):

    name :str
    contactNumber:int
    emailId:str
    occupation: str 
    insuranceType :str
    status:str
    clientUserId:int
    age:int


    

class CreateClient(BaseModel):
    clientUserId:int
    name :str
    companyName :str
    employeeId :int
    insuranceType:str
    password:str





    



