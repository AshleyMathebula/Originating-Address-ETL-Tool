# Originating Address ETL Pipeline

A Python ETL project that extracts originating addresses from a PostgreSQL database, transforms them into the required platform upload format, and loads the final results into a text file.

---

# ETL Flow

```text
Extract  →  Transform  →  Load
Database →  Format     →  Text File
```

---

# What the Project Does

The tool allows a user to enter a `service_id` through the CLI.

It then:

1. Extracts originating addresses from PostgreSQL
2. Cleans and validates the addresses
3. Removes duplicates
4. Converts wildcard patterns
5. Formats addresses into platform-ready regex format
6. Writes the final output to a `.txt` file

---

# Example Transformation

## Input

```text
PROMO?*
```

## Output

```text
regex 1,1,PROMO[0-9]*
```

---

# Project Structure

```text
originating-address-etl/
├── extract/
│   └── db_extractor.py
├── transform/
│   ├── formatter.py
│   └── validator.py
├── load/
│   └── file_writer.py
├── utils/
│   └── logger.py
├── tests/
│   ├── test_db_extractor.py
│   ├── test_file_writer.py
│   ├── test_formatter.py
│   └── test_validator.py
├── main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Tech Stack

- Python
- PostgreSQL
- Neon Database
- Psycopg
- Pytest
- Python-dotenv

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection_string
TEST_SERVICE_ID=TEST_SERVICE
```

Do not commit `.env` to GitHub.

---

# Installation

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the ETL

```bash
python main.py
```

Enter a service ID when prompted:

```text
Enter Service ID: TEST_SERVICE
```

The output file will be created here:

```text
output/cleaned_addresses.txt
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

## Run Transform and Load Tests

```bash
pytest tests/test_formatter.py tests/test_validator.py tests/test_file_writer.py
```

## Run Database Extraction Test

```bash
pytest tests/test_db_extractor.py
```

---

# Tested ETL Stages

| Stage | Tested | Description |
|---|---|---|
| Extract | Yes | Tests database extraction |
| Transform | Yes | Tests validation, deduplication, and formatting |
| Load | Yes | Tests text file generation |

---

# Logging

The project logs ETL status messages for:

```text
START
INPUT
EXTRACT
TRANSFORM
LOAD
END
FAILED
```

Logs are written to:

```text
logs/activity.log
```

---

# Output Format

Each cleaned address is written as:

```text
regex 1,1,<originating_address>
```

Wildcard addresses are converted from:

```text
PROMO?*
```

to:

```text
regex 1,1,PROMO[0-9]*
```

---

# Project Purpose

This project demonstrates:

- Database-driven extraction
- ETL pipeline design
- Modular Python architecture
- SQL querying
- Data validation
- File generation
- Logging
- Automated testing
- Real-world operational workflow

---
