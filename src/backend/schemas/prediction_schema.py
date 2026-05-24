from typing import Dict 
from pydantic import BaseModel


class PredictionRequest(BaseModel):   #input
    disease: str
    features: Dict[str, int | float]


class PredictionResponse(BaseModel):   #output
    disease: str
    prediction: int
    probability: float 