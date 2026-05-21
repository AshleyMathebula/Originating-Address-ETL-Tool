# Originating Address ETL Pipeline

Extracts originating addresses from PostgreSQL, transforms them into platform-ready regex format, and writes the results to a text file.

---

## ETL Flow

```
Extract → Transform → Load
PostgreSQL → Clean / Format → .txt File
```

---

## Usage

Run the pipeline and enter a service ID when prompted:

```bash
python main.py
```

```text
Enter Service ID: TEST_SERVICE
```

Output is written to:

```text
output/cleaned_addresses.txt
```

---

## What It Does

Given a `service_id`, the pipeline:

1. Queries originating addresses from PostgreSQL
2. Validates and cleans addresses
3. Removes duplicates
4. Converts wildcard patterns to regex
5. Writes platform-ready output to a `.txt` file

**Transformation example:**

| Input | Output |
|---|---|
| `PROMO?*` | `regex 1,1,PROMO[0-9]*` |

---

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=your_postgresql_connection_string
TEST_SERVICE_ID=TEST_SERVICE
```

> Do not commit `.env` to version control.

---

## Running Tests

```bash
# All tests
pytest

# Transform and load only
pytest tests/test_formatter.py tests/test_validator.py tests/test_file_writer.py

# Database extraction only
pytest tests/test_db_extractor.py
```

| Stage | Tested | Description |
|---|---|---|
| Extract | ✅ | Database extraction |
| Transform | ✅ | Validation, deduplication, formatting |
| Load | ✅ | Text file generation |

---

## Project Structure

```
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

## Tech Stack

- **Python** — core language
- **PostgreSQL / Neon** — source database
- **Psycopg** — database driver
- **pytest** — test framework
- **python-dotenv** — environment config

---

## Database Query

```sql
SELECT originating_address
FROM service_subscriptions
WHERE service_id = %s
  AND originating_address IS NOT NULL
ORDER BY created_at DESC;
```

---

## Logging

ETL status is logged to `logs/activity.log` across these stages:

```
START → INPUT → EXTRACT → TRANSFORM → LOAD → END
                                             ↓
                                           FAILED (on error)
```

---

## Future Improvements

- Timestamped output files
- ETL run summary report
- Audit table for run history
- CLI arguments in place of manual input
- Optional FastAPI layer
- Scheduled execution
