# Public Data Pipeline

## Problem Statement
This project analyzes 6,451 confirmed exoplanets from the NASA Exoplanet Archive. It explores how discoveries vary by year and discovery method, and summarizes the distances of known exoplanets.

## Tech Stack
- Python 3.13 (standard library only for Stage 1)
- Git for version control
- Data source: NASA Exoplanet Archive (PSCompPars table, retrieved via its TAP service)

## Roadmap
- [x] Stage 1: Read a CSV with plain Python and print a summary report
- [ ] Stage 2: Clean data with pandas and create charts with matplotlib
- [ ] Stage 3: Load data into SQLite and answer questions with SQL
- [ ] Stage 4: Automate the pipeline and publish a Streamlit dashboard
- [ ] Stage 5: Interactive 3D map of exoplanets, with details shown for each selected planet

## Skills Demonstrated
- **Data acquisition**: Downloaded six columns from NASA's TAP service using curl.
- **Data quality**: Reported 28 missing distance values and excluded them from the average distance calculation.
- **Data verification**: Independently counted 6,451 CSV records using PowerShell, matching the Python report.
- **Reproducibility**: Included download instructions; excluded raw data and the virtual environment from Git.
- **Python**: Used CSV reading, loops, dictionaries for frequency counts, and sorting.
- **Version control**: Used Git, a .gitignore file, and an MIT license.

## Setup (Windows PowerShell)
Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Stage 1 uses only Python's standard library and requires no additional packages.

Download the dataset:

```powershell
New-Item -ItemType Directory -Force -Path .\data\raw
curl.exe --fail --location --output .\data\raw\exoplanets.csv "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,discoverymethod,disc_year,sy_dist,pl_rade+from+pscomppars&format=csv"
```

Run the summary from the project root:

```powershell
python .\src\summary.py
```

## Dataset Snapshot
Retrieved: October 19, 2026.

- Planets: 6,451
- Planets with distance values: 6,423
- Planets missing distances: 28
- Average distance: 704.8 parsecs

The archive changes over time, so future downloads may produce different results.

## License
MIT
