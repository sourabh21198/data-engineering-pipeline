# src/cli.py

# fix python path
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import argparse
from src.ingestion.ingest_users import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--landing", required=True)
    args = parser.parse_args()

    run(args.source, args.landing)

if __name__ == "__main__":
    main()
