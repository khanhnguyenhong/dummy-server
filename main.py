# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as dummy_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the routes
app.include_router(dummy_router, prefix="/api")

@app.get("/")
def read_root():
    return {"status": "Dummy Server is running"}