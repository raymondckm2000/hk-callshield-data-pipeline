"""Database connection helpers."""

from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor

from .config import DATABASE_URL


def get_connection() -> psycopg2.extensions.connection:
    """Create a new database connection using the configured URL."""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


@contextmanager
def get_db():
    """Context manager yielding a database connection."""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

