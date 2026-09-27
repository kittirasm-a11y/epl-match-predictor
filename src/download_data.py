from pathlib import Path
from matplotlib.pylab import f
import requests

# E0 = Premier League on football-data.co.uk (capital E, matches their file names)
BASE_URL = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

def season_codes(start=2014, end=2025):
    codes = []
    for year in range(start, end + 1):
        code = str(year)[-2:] + str(year + 1)[-2:]
        codes.append(code)
    return codes

def download_season (season):
    path = RAW_DIR / f"E0_{season}.csv"

    if path.exists():
        print(f"skipping {season} (already downloaded)")
        return

    url = BASE_URL.format(season=season)
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    path.write_bytes(response.content)
    print(f"Downloaded {season} -> {path.name}")

def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for season in season_codes():
        download_season(season)

if __name__ == "__main__": 
        main()

