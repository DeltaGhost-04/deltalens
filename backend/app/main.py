
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(
    title="DeltaLens API",
    description="Mapping and data tools for the Mississippi Delta.",
    version="0.2.0",
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_FILE = PROJECT_ROOT / "frontend" / "index.html"
DATA_FILE = PROJECT_ROOT / "data" / "opportunities.json"


@app.get("/")
def home():
    """Display the DeltaLens map."""
    return FileResponse(FRONTEND_FILE)


@app.get("/api/health")
def health_check():
    """Confirm that the backend is running."""
    return {
        "status": "ok",
        "project": "DeltaLens",
        "version": "0.2.0",
    }


@app.get("/api/opportunities")
def get_opportunities():
    """Return redevelopment records from the JSON dataset."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

        return {
            "count": len(records),
            "records": records,
        }

    except (OSError, json.JSONDecodeError):
        raise HTTPException(
            status_code=500,
            detail="Could not load the redevelopment dataset.",
        )