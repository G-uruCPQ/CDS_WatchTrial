from contextlib import asynccontextmanager
import json
import time
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.database import (
    init_db,
    insert_measurement,
    get_latest_measurement,
    get_history,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Gadgetbridge Data Server",
    version="0.1.0",
    lifespan=lifespan,
)


class Measurement(BaseModel):
    device: str
    kind: str
    observed_at: int
    data: dict[str, Any]


def row_to_dict(row):
    return {
        "id": row["id"],
        "device": row["device"],
        "kind": row["kind"],
        "observed_at": row["observed_at"],
        "received_at": row["received_at"],
        "data": json.loads(row["data"]),
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/api/v1/measurements")
def add_measurement(measurement: Measurement):
    received_at = int(time.time())

    record_id = insert_measurement(
        device=measurement.device,
        kind=measurement.kind,
        observed_at=measurement.observed_at,
        received_at=received_at,
        data=measurement.data,
    )

    return {
        "status": "stored",
        "id": record_id,
    }


@app.get("/api/v1/latest/{kind}")
def latest(kind: str):
    row = get_latest_measurement(kind)

    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for kind={kind}",
        )

    return row_to_dict(row)


@app.get("/api/v1/history/{kind}")
def history(
    kind: str,
    limit: int = 100,
):
    limit = min(max(limit, 1), 1000)

    rows = get_history(kind, limit)

    return [
        row_to_dict(row)
        for row in rows
    ]