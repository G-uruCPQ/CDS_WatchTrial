import json
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "gadgetbridge.db"


def connect_db():
    conn = sqlite3.connect(DB_PATH, timeout=5)
    conn.row_factory = sqlite3.Row

    # 読み書きを並行しやすくする
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")

    return conn


def init_db():
    with connect_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device TEXT NOT NULL,
                kind TEXT NOT NULL,
                observed_at INTEGER NOT NULL,
                received_at INTEGER NOT NULL,
                data TEXT NOT NULL
            )
            """
        )

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_measurements_kind_time
            ON measurements(kind, observed_at)
            """
        )


def insert_measurement(
    device: str,
    kind: str,
    observed_at: int,
    received_at: int,
    data: dict
):
    with connect_db() as conn:
        cursor = conn.execute(
            """
            INSERT INTO measurements (
                device,
                kind,
                observed_at,
                received_at,
                data
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                device,
                kind,
                observed_at,
                received_at,
                json.dumps(data, ensure_ascii=False),
            ),
        )

        return cursor.lastrowid


def get_latest_measurement(kind: str):
    with connect_db() as conn:
        row = conn.execute(
            """
            SELECT *
            FROM measurements
            WHERE kind = ?
            ORDER BY observed_at DESC
            LIMIT 1
            """,
            (kind,),
        ).fetchone()

    return row


def get_history(kind: str, limit: int):
    with connect_db() as conn:
        rows = conn.execute(
            """
            SELECT *
            FROM measurements
            WHERE kind = ?
            ORDER BY observed_at DESC
            LIMIT ?
            """,
            (kind, limit),
        ).fetchall()

    return rows