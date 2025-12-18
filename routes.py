# routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import trafilatura
import os

# Create a router (like a mini-app)
router = APIRouter()

DATA_FILE = "scraped_data.txt"

# Data Model
class UrlRequest(BaseModel):
    url: str

@router.post("/scrape")
async def scrape_and_save(request: UrlRequest):
    """
    Fetches URL, extracts text using AI heuristics, and saves to file.
    """
    downloaded = trafilatura.fetch_url(request.url)
    
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