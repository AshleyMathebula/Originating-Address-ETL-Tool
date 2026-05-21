import os

import pytest
from dotenv import load_dotenv

from extract.db_extractor import fetch_originating_addresses


load_dotenv()


@pytest.mark.integration
def test_fetch_originating_addresses_real_database():
    """
    Real database integration test.

    This connects to the actual PostgreSQL database.
    Use TEST_SERVICE_ID in .env for a service_id that exists in your test/sample data.
    """

    service_id = os.getenv("TEST_SERVICE_ID")

    if not service_id:
        pytest.skip("TEST_SERVICE_ID not set in .env file.")

    result = fetch_originating_addresses(service_id)

    assert isinstance(result, list)

    for address in result:
        assert isinstance(address, str)
        assert address.strip() != ""