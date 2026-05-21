"""
validator.py

Cleans, validates, removes duplicates, and formats addresses for upload.
"""

import re
from typing import List
from utils.logger import log_info, log_warning
from transform.formatter import format_address


def clean_validate_and_format(raw_addresses: List[str]) -> List[str]:
    """
    Processes a list of raw addresses for upload.

    Steps:
    1. Cleans stray characters like '?'
    2. Detects addresses containing '?*' and counts them
    3. Removes duplicates while logging them
    4. Validates allowed characters (letters, digits, '*')
    5. Formats for the target system using format_address()

    Args:
        raw_addresses (List[str]): List of raw originating addresses

    Returns:
        List[str]: Cleaned, unique, formatted addresses
    """


    # List to store the final cleaned and formatted addresses
    # This will hold all valid, unique addresses after processing
    cleaned_addresses: List[str] = []

    # Set to keep track of addresses we've already seen
    # Used for deduplication, since sets provide O(1) lookup time
    seen: set[str] = set()

    # List to store duplicate raw addresses that were skipped
    # This is mainly for logging purposes so the user knows which entries were duplicates
    duplicates: List[str] = []

    # Counter to track how many addresses contained the '?*' pattern
    # Useful for logging and reporting pattern occurrences
    count_qs_pattern = 0

    for raw in raw_addresses:
        raw = raw.strip()  # Remove leading/trailing whitespace
        if not raw:
            # Skip empty lines or entries
            continue

        # Count addresses containing '?*'
        if "?*" in raw:
            count_qs_pattern += 1

        # Remove any stray '?' for base validation
        base_address = raw.replace("?", "")

        # Validate allowed characters: letters, digits, and '*'
        # Skip and log invalid entries
        if not re.match(r"^[A-Za-z0-9*]+$", base_address):
            log_warning(f"Invalid format skipped: {raw}")
            continue

        # Deduplicate: skip if we've already seen this base address
        if base_address in seen:
            duplicates.append(raw)  # Keep original raw for logging
            continue

        # Add base address to 'seen' set
        seen.add(base_address)

        # Format the address for upload
        # format_address automatically handles '?*' pattern
        formatted = format_address(raw)

        # Add formatted address to final list
        cleaned_addresses.append(formatted)

    if duplicates:
        # Log how many duplicates were found
        log_info(f"Found {len(duplicates)} duplicate(s): {duplicates}")
    else:
        log_info("No duplicates found.")

    # Log number of tagging addresses '?*'
    log_info(f"Tagging addresses  '?*': {count_qs_pattern}")

    # Optional: sort addresses for consistent output
    cleaned_addresses.sort()

    # Return final cleaned, unique, and formatted list
    return cleaned_addresses



