from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd

# Configurar FastAPI
app = FastAPI(title="Penguins Classification API", version="1.0")

# Configurar MLflow Tracking Server
MLFLOW_TRACKING_URI = "http://10.43.101.187:5000"
MODEL_NAME = "penguins_best_model"
MODEL_VERSION = "1"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Cargar el modelo desde MLflow Model Registry
model = mlflow.pyfunc.load_model(model_uri=f"models:/{MODEL_NAME}/{MODEL_VERSION}")

@app.get("/")
def home():
    return {"message": "¡Bienvenido a la API de clasificación de pingüinos!"}

@app.post("/predict/")
def predict(culmen_length_mm: float, culmen_depth_mm: float, flipper_length_mm: float, body_mass_g: float):
    """
    Realiza una predicción del sexo del pingüino basándose en sus características.
    """
    # Crear un DataFrame con la entrada
    input_data = pd.DataFrame([{
        "culmen_length_mm": culmen_length_mm,
        "culmen_depth_mm": culmen_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g
    }])

    # Realizar predicción
    prediction = model.predict(input_data)

    # Interpretar resultado
    result = "MACHO" if prediction[0] == 1 else "HEMBRA"

    return {"prediction": result}
