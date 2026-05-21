"""
main.py

CLI entry point for the Originating Address ETL Tool.

ETL flow:
E - Extract originating addresses from PostgreSQL
T - Clean, validate, deduplicate, and format addresses
L - Load/write formatted addresses to a text file
"""

from extract.db_extractor import fetch_originating_addresses
from transform.validator import clean_validate_and_format
from load.file_writer import write_output_file
from utils.logger import log_info, log_success, log_error


def main():
    """Main ETL workflow."""

    output_path = "output/cleaned_addresses.txt"

    try:
        service_id = input("Enter Service ID: ").strip()

        if not service_id:
            log_error("[INPUT] Service ID cannot be empty.")
            return

        log_info("[START] ETL process started.")
        log_info(f"[INPUT] Service ID received: {service_id}")

        # EXTRACT
        log_info("[EXTRACT] Starting database extraction...")
        raw_addresses = fetch_originating_addresses(service_id)

        if not raw_addresses:
            log_error(f"[EXTRACT] No originating addresses found for service_id: {service_id}")
            return

        log_success(f"[EXTRACT] Extraction completed. Total extracted: {len(raw_addresses)}")

        # TRANSFORM
        log_info("[TRANSFORM] Starting validation, deduplication, and formatting...")
        formatted_addresses = clean_validate_and_format(raw_addresses)

        if not formatted_addresses:
            log_error("[TRANSFORM] No valid addresses available after transformation.")
            return

        log_success(
            f"[TRANSFORM] Transformation completed. Final count: {len(formatted_addresses)}"
        )

        # LOAD
        log_info("[LOAD] Writing transformed addresses to output file...")
        write_output_file(output_path, formatted_addresses)

        log_success(f"[LOAD] Output file created: {output_path}")
        log_success("[END] ETL process completed successfully.")

    except Exception as e:
        log_error(f"[FAILED] ETL process failed: {e}")


if __name__ == "__main__":
    main()