
from fastapi import FastAPI
import pandas as pd, os

app=FastAPI()

@app.get("/violations")
def get_violations():
    if not os.path.exists("../logs/violations.csv"):
        return []
    df=pd.read_csv("../logs/violations.csv")
    return df.to_dict(orient="records")
