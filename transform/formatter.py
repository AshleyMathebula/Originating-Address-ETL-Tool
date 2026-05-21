"""
formatter.py

Formats cleaned originating addresses into the target platform format.

Standard:
regex 1,1,<address>

Wildcard:
PROMO?* becomes regex 1,1,PROMO[0-9]*
"""

from typing import List


def format_address(address: str) -> str:
    """
    Format a single cleaned address for upload.
    """

    if not address:
        raise ValueError("[ERROR] Address cannot be empty.")

    if "?*" in address:
        address_cleaned = address.replace("?*", "")
        return f"regex 1,1,{address_cleaned}[0-9]*"

    return f"regex 1,1,{address}"


def format_addresses(addresses: List[str]) -> List[str]:
    """
    Format a list of addresses.
    """

    return [format_address(addr) for addr in addresses]