import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import storage

app = FastAPI(title="Retail Sales Prediction API")

FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://127.0.0.1:5500")
BUCKET_NAME = os.environ.get("MODEL_BUCKET", "satis-modelleri")
LGBM_FILE = os.environ.get("LGBM_FILE", "lightgbm_model.pkl")
CATBOOST_FILE = os.environ.get("CATBOOST_FILE", "catboost_model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:5500"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

def load_model_from_gcs(bucket_name, file_name):
    if os.path.exists(file_name):
        try:
            model = joblib.load(file_name)
            return model
        except Exception as e:
            print(f"Model yüklenirken hata oluştu: {e}")
            return None
    path = f"/tmp/{file_name}"
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.download_to_filename(path)
        model = joblib.load(path)
        os.remove(path)
        return model
    except Exception as e:
        print(f"Model yüklenirken hata oluştu: {e}")
        return None

lgbm_model = load_model_from_gcs(BUCKET_NAME, LGBM_FILE)
catboost_model = load_model_from_gcs(BUCKET_NAME, CATBOOST_FILE)

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

@app.post("/predict/lgbm")
async def predict_lgbm(data: InputData):
    if not lgbm_model:
        raise HTTPException(status_code=500, detail="LGBM model could not be loaded")

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
    prediction = lgbm_model.predict(input_array)
    return {"predicted_sales": f"{prediction[0]:.2f}"}

@app.post("/predict/catboost")
async def predict_catboost(data: InputData):
    if not catboost_model:
        raise HTTPException(status_code=500, detail="CatBoost model could not be loaded")

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
    prediction = catboost_model.predict(input_array)
    return {"predicted_sales": f"{prediction[0]:.2f}"}

@app.post("/predict/stacked")
async def predict_stacked(data: InputData):
    if not lgbm_model or not catboost_model:
        raise HTTPException(status_code=500, detail="One or more models could not be loaded")

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
    lgbm_pred = lgbm_model.predict(input_array)
    catboost_pred = catboost_model.predict(input_array)
    stacked_pred = (lgbm_pred + catboost_pred) / 2
    return {"predicted_sales": f"{stacked_pred[0]:.2f}"}