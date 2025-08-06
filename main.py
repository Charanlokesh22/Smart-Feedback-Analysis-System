from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .auth import get_current_user
from .monitor import get_system_metrics
from .models import User

app = FastAPI(title="Smart Resource Monitor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smart Resource Monitor API is running"}

@app.get("/metrics/")
def metrics(user: User = Depends(get_current_user)):
    return get_system_metrics()
