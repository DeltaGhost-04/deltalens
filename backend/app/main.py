
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="DeltaLens API",
    description="Mapping and data tools for the Mississippi Delta.",
    version="0.1.0",
)

# Locate frontend/index.html relative to this Python file.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_FILE = PROJECT_ROOT / "frontend" / "index.html"


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
        "version": "0.1.0",
    }