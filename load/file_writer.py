"""
file_writer.py

Handles file reading and writing for the Originating Address Cleaner Tool.
"""

from pathlib import Path
import re
from typing import List


def read_input_file(filepath: str) -> List[str]:
    """
    Reads originating addresses from a text file.
    Handles flexible input formats:
    - One address per line
    - Comma, semicolon, or space separated values
    - Mixed formats

    Args:
        filepath (str): Path to the input .txt file.

    Returns:
        List[str]: List of originating address strings.
    """
    file_path = Path(filepath)
    if not file_path.exists():
        raise FileNotFoundError(f"[ERROR] File not found: {filepath}")

    addresses = []

    try:
        # Process file line by line for memory efficiency
        with file_path.open("r", encoding="utf-8") as file:
            for line in file:
                # Split by commas, semicolons, spaces, or newlines
                raw = re.split(r"[,\s;]+", line.strip())
                addresses.extend([addr.strip() for addr in raw if addr.strip()])
    except OSError as e:
        raise OSError(f"[ERROR] Failed to read file {filepath}: {e}")

    return addresses


def write_output_file(filepath: str, addresses: List[str]) -> None:
    """
    Writes cleaned originating addresses to a text file.
    Creates parent directories if they don't exist.

    Args:
        filepath (str): Path where the cleaned file will be saved.
        addresses (List[str]): List of cleaned originating addresses.
    """
    file_path = Path(filepath)
    # Ensure parent directory exists
    if file_path.parent:
        file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with file_path.open("w", encoding="utf-8") as file:
            for address in addresses:
                file.write(f"{address}\n")
    except OSError as e:
        raise OSError(f"[ERROR] Failed to write file {filepath}: {e}")

