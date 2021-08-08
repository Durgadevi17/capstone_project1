

from fastapi import Request,FastAPI
import joblib
from classification import classify_message

app = FastAPI()

model = joblib.load('text_classifier.joblib')  
    
@app.get("/")
async def root():
    return {"message": "Hello World"}
   
@app.get("/message/{tweet_message}")
async def read_item(tweet_message: str):
    l=classify_message(model,tweet_message)
    return {"message": str(l)}
    
@app.post("/message1/predict")
async def read_item_post(request: Request):
    input_data = await request.json()
    l=classify_message(model,input_data['data'])
    return {"message": str(l)}
    