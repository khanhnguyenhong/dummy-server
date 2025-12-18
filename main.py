# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as dummy_router  # Import the router we just made

app = FastAPI()

# Enable CORS so your React/Angular apps can talk to this Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the routes
# You can add a prefix if you want, e.g., prefix="/api/v1"
app.include_router(dummy_router)

@app.get("/")
def read_root():
    return {"status": "Dummy Server is running"}