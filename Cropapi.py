import uvicorn
from fastapi import FastAPI
from Cropclass import Cropdata , CropdataReq
import pickle
import pandas as pd

app = FastAPI()
   
# Load the model from pickle file

gb_model = pickle.load(open("gb_model.pkl", "rb"))

##############################################################################################################

@app.post("/")
async def CropPrediction(data:CropdataReq):
    Data = data.model_dump()
    

    df = pd.DataFrame(Data, index =[0])
  
    predicted_values = gb_model.predict(df)
    predicted_values_serializable = predicted_values.tolist()
    return {"Prediction" : predicted_values_serializable}