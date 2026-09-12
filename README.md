# Public Data Pipeline

## Problem Statement
This project analyzes 6,360 confirmed exoplanets from the NASA Exoplanet Archive. It asks how the discovery of these planets has changed throughout the years and compares the distance at which we are finding the most exoplanets and the discovery methods used. The results show how planet-hunting methods have shaped what we know. Knowing this information may influence future discovery patterns allowing scientists to refine their approaches for discovering new exoplanets.

## Tech Stack
- Python 3.13 (standard library only for Stage 1)
- Git for version control
- Data source: NASA Exoplanet Archive (PSCompPars table, retrieved via its TAP service)

## Roadmap
- [ ] Stage 1: Read a CSV with plain Python and print a summary report
- [ ] Stage 2: Clean data with pandas and create charts with matplotlib
- [ ] Stage 3: Load data into SQLite and answer questions with SQL
- [ ] Stage 4: Automate the pipeline and publish a Streamlit dashboard
- [ ] Stage 5: Interactive 3D map of exoplanets, with details shown for each selected planet

## Skills Demonstrated
[Fill in as each stage is completed. List only skills actually shown in this repo.]

## Setup
```
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Download the dataset (not stored in this repository):
```
mkdir -p data/raw
curl -o data/raw/exoplanets.csv "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,discoverymethod,disc_year,sy_dist,pl_rade+from+pscomppars&format=csv"
```
## License
MIT
