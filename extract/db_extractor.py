"""
db_extractor.py

Extracts originating addresses from PostgreSQL based on service_id.
"""

import os
from typing import List

import psycopg
from dotenv import load_dotenv

from utils.logger import log_info, log_success


load_dotenv()


def get_connection():
    """Create and return a PostgreSQL database connection."""

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("[ERROR] DATABASE_URL not found in .env file.")

    log_info("[EXTRACT] Connecting to PostgreSQL database...")

    connection = psycopg.connect(database_url)

    log_success("[EXTRACT] Database connection successful.")

    return connection


def fetch_originating_addresses(service_id: str) -> List[str]:
    """
    Fetch originating addresses for a specific service_id.

    Args:
        service_id (str): Service ID entered by the user.

    Returns:
        List[str]: List of originating addresses.
    """

    query = """
    SELECT
        originating_address
    FROM
        service_subscriptions
    WHERE
        service_id = %s
        AND originating_address IS NOT NULL
    ORDER BY
        created_at DESC;
    """

    log_info("[EXTRACT] Running SQL query...")

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (service_id,))
            rows = cursor.fetchall()

    addresses = [row[0] for row in rows]

    log_success(f"[EXTRACT] Extracted {len(addresses)} address(es).")

    return addresses