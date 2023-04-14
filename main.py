from fastapi import FastAPI
from routers import customers,unnatiClients
import models
from database import engine


models.Base.metadata.create_all(engine)


app = FastAPI()

app.include_router(unnatiClients.router)
app.include_router(customers.router)
