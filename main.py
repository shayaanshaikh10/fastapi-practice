from fastapi import FastAPI

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
