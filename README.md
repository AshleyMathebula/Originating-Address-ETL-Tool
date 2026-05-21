# ORIGINATING-ADDRESS-CLEANER-TOOL

*Streamline Addresses cleaning, Accelerate Success, Ensure Precision.*

![Last Commit](https://img.shields.io/github/last-commit/AshleyMathebula/Originating-Address-Cleaner-Tool?color=blue)
![Python](https://img.shields.io/badge/python-100%25-blue)
![Language Count](https://img.shields.io/github/languages/count/AshleyMathebula/Originating-Address-Cleaner-Tool?color=brightgreen)

---

### Built:
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)



---

## 🗂️ Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Logging](#logging)
- [License](#license)

---

## 🧩 Overview

The **Originating Address Cleaner Tool** is a robust utility for **validating**, **formatting**, and **deduplicating** raw originating address data.  
It transforms unstructured input files into clean, standardized datasets ready for upload or system integration.

This tool implements a **Linear ETL (Extract, Transform, Load)** pipeline:
- **Extract:** Reads address data from text files.  
- **Transform:** Cleans, validates, and formats using pattern recognition and deduplication logic.  
- **Load:** Writes the final output to structured text files, logging all operations.

This design ensures **data integrity**, **traceability**, and **automation-readiness** for large-scale data preprocessing tasks.

---

### 💡 Why Originating-Address-Cleaner-Tool?

This project simplifies address preprocessing workflows by ensuring data integrity and consistency across environments.

**Core Features:**
- Reads flexible input formats (line-based, comma, semicolon, or space-separated)
- Cleans invalid characters and detects `?*` patterns
- Removes duplicates and invalid data
- Converts cleaned data to regex upload format
- Logs all activity for full traceability

## 🚀 Getting Started

### 🧰 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python 3.9+
- **Package Manager:** pip

---

### ⚙️ Installation

Build **Originating-Address-Cleaner-Tool** from source and install dependencies.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AshleyMathebula/Originating-Address-Cleaner-Tool
   
2. **Navigate to the project directory:**

    ```bash
    cd Originating-Address-Cleaner-Tool

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt

## ▶️ Usage
Run the tool to execute the complete ETL pipeline:

    bash
    python main.py
    
Default paths:

    Input: data/input_addresses.txt
    
    Output: output/cleaned_addresses.txt
    
    Logs: logs/activity.log

Example output:

    regex 1,1,ABC123
    regex 1,1,XYZ[0-9]*
    regex 1,1,DEF001

## 🧾 Logging

All tool activities are logged both to console and file (logs/activity.log):

Log Levels:

    [INFO] General information (file loaded, steps completed)
    
    [SUCCESS] Successful operations
    
    [WARN] Skipped or invalid data entries
    
    [ERROR] File or runtime errors

Example Log:

    2025-10-27 | INFO | Loaded 534 addresses from data/input_addresses.txt
    2025-10-27 | INFO | Found 12 duplicate(s)
    2025-10-27 | SUCCESS | Cleaned addresses written to output/cleaned_addresses.txt

## 🪪 License

This project is developed and maintained by Ashley Mathebula.
