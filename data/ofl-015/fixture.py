"""Small provisional OFL-015 fixture; Python 3 standard library only."""

import argparse
import csv
import hashlib
import json
import random
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLUMNS = [
    "transaction_id", "transaction_date", "amount", "currency", "error_ids"
]
SEED = 15024
ROW_COUNT = 26


def detect(row):
    """Return all applicable defect IDs, independently of the truth label."""
    errors = set()
    if not row["amount"]:
        errors.add("E01")
    elif not re.fullmatch(r"-?(0|[1-9][0-9]*)\.[0-9]{2}", row["amount"]):
        errors.add("E03")
    try:
        date.fromisoformat(row["transaction_date"])
        if not re.fullmatch(
            r"[0-9]{4}-[0-9]{2}-[0-9]{2}", row["transaction_date"]
        ):
            errors.add("E02")
    except ValueError:
        errors.add("E02")
    if not re.fullmatch(r"[A-Z]{3}", row["currency"]):
        errors.add("E04")
    return errors


def generate():
    rng = random.Random(SEED)
    mutations = {
        3: (("amount", "", "E01"),),
        7: (("transaction_date", "2026-02-30", "E02"),),
        11: (("amount", "12x.50", "E03"),),
        15: (("currency", "US$", "E04"),),
        19: (("amount", "", "E01"),),
        23: (("transaction_date", "not-a-date", "E02"),),
        25: (("amount", "", "E01"), ("transaction_date", "2026-02-30", "E02")),
        26: (("amount", "12x.50", "E03"), ("currency", "US$", "E04")),
    }
    with (ROOT / "transactions.csv").open(
        "w", encoding="utf-8", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream, fieldnames=COLUMNS, lineterminator="\n"
        )
        writer.writeheader()
        for index in range(1, ROW_COUNT + 1):
            cents = rng.randint(100, 99999)
            row = dict(zip(COLUMNS, [
                f"SYN-{index:03d}",
                (date(2026, 1, 1) + timedelta(days=index - 1)).isoformat(),
                f"{cents // 100}.{cents % 100:02d}", "USD", "",
            ]))
            errors = []
            for column, value, error in mutations.get(index, ()):
                row[column] = value
                errors.append(error)
            row["error_ids"] = ";".join(sorted(errors))
            writer.writerow(row)
    digest = hashlib.sha256(
        (ROOT / "transactions.csv").read_bytes()
    ).hexdigest()
    print(f"Generated {ROW_COUNT} rows; seed={SEED}; sha256={digest}")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    ids = [entry["id"] for entry in catalog]
    require(len(ids) == len(set(ids)) and
            set(ids) == {"E01", "E02", "E03", "E04"},
            "Catalog IDs differ from implemented rules")
    with (ROOT / "transactions.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        reader = csv.DictReader(stream)
        require(reader.fieldnames == COLUMNS, "Unexpected columns/order")
        rows = list(reader)
    require(len(rows) == ROW_COUNT, "Unexpected row count")
    counts = Counter()
    examples = {error: [] for error in ids}
    clean = 0
    multiple = 0
    for index, row in enumerate(rows, 1):
        require(None not in row and
                all(value is not None for value in row.values()),
                f"Malformed CSV record {index}")
        require(row["transaction_id"] == f"SYN-{index:03d}",
                f"Invalid ID at {index}")
        labels = row["error_ids"].split(";") if row["error_ids"] else []
        require(len(labels) == len(set(labels)) and set(labels) <= set(ids),
                f"Invalid labels at {index}")
        require(labels == sorted(labels),
                f"Noncanonical label order at {index}")
        detected = detect(row)
        require(detected == set(labels),
                f"Rule/truth mismatch at {index}: {detected} / {labels}")
        clean += not detected
        multiple += len(detected) > 1
        counts.update(detected)
        for error in detected:
            examples[error].append(row["transaction_id"])
    require(clean > 0, "No clean controls")
    require(multiple > 0, "No multi-error rows")
    for entry in catalog:
        require(counts[entry["id"]] > 0, f"Missing defect {entry['id']}")
        require(examples[entry["id"]] == entry["example_transaction_ids"],
                f"Catalog examples mismatch: {entry['id']}")
    print(f"PASS rows={len(rows)} columns={','.join(COLUMNS)} "
          f"clean={clean} defective={len(rows) - clean}")
    print(f"single_error={len(rows) - clean - multiple} "
          f"multi_error={multiple}")
    for error in sorted(counts):
        print(f"{error}: {counts[error]} rows ({', '.join(examples[error])})")
    print("PASS catalog coverage; exact truth/rule agreement; "
          "all clean rows pass")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["generate", "validate"])
    args = parser.parse_args()
    try:
        {"generate": generate, "validate": validate}[args.action]()
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")
