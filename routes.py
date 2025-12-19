# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import trafilatura
import os
import datetime

# Create a router (like a mini-app)
router = APIRouter()

DATA_FILE = "./data/scraped_data.txt"
HISTORY_FILE = "./data/history.txt"

# Data Model
class UrlRequest(BaseModel):
    url: str

@router.post("/scrape")
async def scrape_and_save(request: UrlRequest):
    """
    Fetches URL, extracts text using AI heuristics, and saves to file.
    """
    downloads = trafilatura.fetch_url(request.url)
    
    # Log to history
    timestamp = datetime.datetime.now().isoformat()
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {request.url}\n")
    except Exception as e:
        print(f"Error logging history: {e}")

    downloaded = downloads
    
    if not downloaded:
        raise HTTPException(status_code=400, detail="Could not fetch the URL")

    # Extract clean text
    text_content = trafilatura.extract(downloaded)

    if not text_content:
        raise HTTPException(status_code=400, detail="No readable text found")

    # Save to file
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(text_content)

    return {
        "status": "success", 
        "message": "Data saved successfully", 
        "preview": text_content[:200] + "..."
    }

@router.get("/data")
async def get_saved_data():
    """
    Returns the content of the saved text file.
    """
    if not os.path.exists(DATA_FILE):
        return {"content": ""}
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    return {"content": content}

@router.get("/fetch-history")
async def get_history():
    """
    Returns the last 20 requests.
    """
    if not os.path.exists(HISTORY_FILE):
        return {"history": []}
    
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Get last 20 lines
    last_20 = lines[-20:]
    return {"history": [line.strip() for line in last_20]}