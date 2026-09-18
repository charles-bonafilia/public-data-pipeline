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
- **Data acquisition**: Utilized NASA's TAP service using command-line (`curl`); a 6-column subset archive retrieved
- **Data quality**: Excluded 28 missing distance values explicitly when calculating mean distance of discovered planets; exclusion reported alongside the average
- **Data verification**: Cross-checked Python results against independent command-line counts (`wc -l`, `grep`, `cut`, `sort`, `uniq`); all three tallies sum to 6,360 planets
- **Reproducibility**: No raw data included in the repo; README provides download instructions
- **Python**: CSV reading, loops, dictionaries for frequency counts, sorting by key and by value
- **Analytical interpretation**: 2014 and 2016 spikes reflect bulk confirmation methods, so `disc_year` measures confirmation methodology rather than detection capability
- **Version control**: 6 commits, `.gitignore` excluding raw data and `.venv`; MIT license; private commit email



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
