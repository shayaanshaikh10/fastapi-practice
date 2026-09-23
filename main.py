from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class LinkRequest(BaseModel):
    deal_id:int
    amount:float 

app=FastAPI()

@app.get("/")
def home():
    return {"status":"server is running"}

@app.get("/deals/{deal_id}")
def get_deal(deal_id:int):
    return {"deal_id":deal_id,"amount": 5000}

@app.get("/search")
def search(name:str="shayaan",limit:int=5):
    return {"name":name,"limit":limit}

@app.post("/create-link")
def creat_link(data:LinkRequest):
    if data.deal_id<1:
        return HTTPException(status_code=400,detail="deal id should be postive")
    if data.amount<=0:
        return HTTPException(status_code=400,detail="amount must be greater than zero")
    return{
        "message":"would create a link here",
        "deal_id":data.deal_id,
        "amount:":data.amount
    }
