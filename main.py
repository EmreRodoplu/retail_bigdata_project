import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
frontend_url = os.environ.get("FRONTEND_URL", "http://127.0.0.1:5500")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://localhost:5500"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)
model = joblib.load("lightgbm_model.pkl")
bagimsiz_degiskenler = [
    'urunklasmankod', 
    'satisadet_lfl_gy',       
    'indirimorani', 
    'gunlukminimumsicaklik', 
    'gunlukortalamasicaklik', 
    'gunlukmaksimumsicaklik', 
    'ozelgunflag', 
    'gunsonutoplamstok', 
    'gunsonureyonstok', 
    'Haftanin_Gunu', 
    'Yilin_Ayi',              
    'Yilin_Haftasi',          
    'Acik_Kalma_Suresi_Saat', 
    'ulke_Index', 
    'magazakod_Index', 
    'merchmarkayasgrupkod_Index', 
    'merchaltgrupkod_Index', 
    'depoyerlesimtip_Index',
    'Haftasonu_Mu',
    'Indirim_x_Haftasonu'
]

class InputData(BaseModel):
    urunklasmankod: int
    satisadet_lfl_gy: int
    indirimorani: float
    gunlukminimumsicaklik: float
    gunlukortalamasicaklik: float
    gunlukmaksimumsicaklik: float
    ozelgunflag: int
    gunsonutoplamstok: int
    gunsonureyonstok: int
    Haftanin_Gunu: int
    Yilin_Ayi: int
    Yilin_Haftasi: int
    Acik_Kalma_Suresi_Saat: float
    ulke_Index: int
    magazakod_Index: int
    merchmarkayasgrupkod_Index: int
    merchaltgrupkod_Index: int
    depoyerlesimtip_Index: int
    Haftasonu_Mu: int
    Indirim_x_Haftasonu: float

@app.post("/predict")
async def predict(data: InputData):
    input_array = np.array([[
        data.urunklasmankod,
        data.satisadet_lfl_gy,
        data.indirimorani,
        data.gunlukminimumsicaklik,
        data.gunlukortalamasicaklik,
        data.gunlukmaksimumsicaklik,
        data.ozelgunflag,
        data.gunsonutoplamstok,
        data.gunsonureyonstok,
        data.Haftanin_Gunu,
        data.Yilin_Ayi,
        data.Yilin_Haftasi,
        data.Acik_Kalma_Suresi_Saat,
        data.ulke_Index,
        data.magazakod_Index,
        data.merchmarkayasgrupkod_Index,
        data.merchaltgrupkod_Index,
        data.depoyerlesimtip_Index,
        data.Haftasonu_Mu,
        data.Indirim_x_Haftasonu
    ]])
    prediction = model.predict(input_array)
    return {"predicted_sales": f"{prediction[0]:.2f}"}