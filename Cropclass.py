from pydantic import BaseModel , Field

# This Class describes the Crop data measurments.
class Cropdata:
    N: int           
    P: int          
    K: int          
    temperature: float
    humidity: float  
    ph: float          
    rainfall: float

    def _init_(self,N,P,K,temperature,humidity,ph,rainfall):
        self.N = N
        self.P = P
        self.K = K
        self.temperature = temperature
        self.humidity = humidity
        self.ph = ph
        self.rainfall = rainfall

class CropdataReq(BaseModel):
    N: int = Field(gt=-1,lt=101)          
    P: int = Field(gt=-1,lt=101)         
    K: int = Field(gt=-1,lt=101)         
    temperature: float = Field(gt=-1,lt=101.00)
    humidity: float = Field(gt=-1,lt=101.00)
    ph: float  = Field(gt=-1,lt=15.00)      
    rainfall: float = Field(gt=-1,lt=101.00)