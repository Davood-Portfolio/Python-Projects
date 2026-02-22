import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/database.db")

def load_from_sqlite(query: str) -> pd.DataFrame:
    """Load data from SQLite database using a SQL query."""
    if not DB_PATH.exists():
        raise FileNotFoundError("SQLite database not found in /data directory")

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def load_from_csv(csv_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    return pd.read_csv(path)
