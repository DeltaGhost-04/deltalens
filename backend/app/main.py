
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ValidationError

app = FastAPI(
    title="DeltaLens API",
    description="Mapping and data tools for the Mississippi Delta.",
    version="0.2.0",
)

class OpportunityRecord(BaseModel):
    id: str
    name: str

    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

    status: str
    category: str

    source: str
    last_verified: Optional[date] = None
    notes: str = ""

    # Additional fields for future real-world records
    county: Optional[str] = None
    parcel_id: Optional[str] = None
    address: Optional[str] = None
    evidence_type: Optional[str] = None
    source_url: Optional[str] = None
    source_retrieved_at: Optional[date] = None

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
    """Return validated redevelopment records from the JSON dataset."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise HTTPException(
                status_code=500,
                detail="The dataset must contain a list of records.",
            )

        validated_records = [
            OpportunityRecord.parse_obj(record)
            for record in records
        ]

        return {
            "count": len(validated_records),
            "records": [
                record.dict()
                for record in validated_records
            ],
        }

    except (OSError, json.JSONDecodeError):
        raise HTTPException(
            status_code=500,
            detail="Could not load the redevelopment dataset.",
        )

    except ValidationError as error:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "A record failed validation.",
                "errors": error.errors(),
            },
        )