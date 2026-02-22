 DataInsight Engine
A modular Python engine for data processing, analytics, and CLI‑based insights.

DataInsight Engine is designed for real‑world data workflows including cleaning, transformation, log processing, and generating analytical summaries.
Its modular architecture allows you to build custom pipelines, extend functionality, and run analysis directly from the command line.

 Features
Data cleaning & preprocessing

Log parsing and transformation

CLI interface for running analysis

Modular engine architecture

Support for custom processing pipelines

Includes unit tests

Easy to extend and integrate into larger systems

Project Structure

DataInsight-Engine/
│── cli/               # CLI entry point
│── engine/            # Core processing and analytics modules
│   ├── processors/    # Data cleaning, parsing, transformations
│   ├── analytics/     # Summary statistics, frequency analysis, etc.
│── data/              # Sample datasets
│── tests/             # Unit tests
│── README.md
│── requirements.txt

 Installation

git clone https://github.com/Davood-Portfolio/Python-Projects.git
cd DataInsight-Engine
pip install -r requirements.txt

Usage
Run a summary analysis:

python cli/main.py --input data/sample.csv --analyze summary

Clean a raw log file:

python cli/main.py --clean data/raw_logs.txt

Run a frequency analysis on a specific column:

python cli/main.py --analyze frequency --column user_id

Running Tests
pytest

 Technologies Used
Python 3.x

pandas

argparse

pytest

 License
MIT License
Open for contributions.