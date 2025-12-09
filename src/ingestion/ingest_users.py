import argparse
import csv
import logging
from datetime import datetime
from pathlib import Path
import os
print("PYTHON WORKING DIRECTORY:", os.getcwd())

logger = logging.getLogger("ingest")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_output(records, out_dir):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    output_file = Path(out_dir) / f"users_{ts}.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    return str(output_file)


def run(source, landing):
    logger.info("Reading file from: %s", source)
    records = read_csv(source)
    logger.info("Total records: %d", len(records))

    output = write_output(records, landing)
    logger.info("File written to: %s", output)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--landing", required=True)
    args = parser.parse_args()

    run(args.source, args.landing)
import os
from pathlib import Path


