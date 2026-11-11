# OFL-015 — Small Synthetic Fixture

**PROVISIONAL — pending confirmation.** This schema and its rules are local
assumptions for review with Brian; they are neither the official OFL-009 schema
nor the valid OFL-010 dataset. The requirements in
[issue #24](https://github.com/hansen-ai-service/OpenFinanceLab/issues/24)
call for missing amounts, invalid dates, and malformed fields, with each defect
identifiable. This fixture contains 26 invented transactions with no people or
accounts: 18 clean controls and 8 defective rows (6 with a single error and 2
with multiple simultaneous errors). It is not a complete dataset.

## Schema: PROVISIONAL — pending confirmation

The CSV uses UTF-8 without a BOM, comma delimiters, a header, and LF line endings.
An empty cell represents a missing value. All columns are required; `error_ids`
is empty for clean rows. Defective rows deliberately violate the stated rules.

| Column | Logical type / format | Assumption |
|---|---|---|
| transaction_id | Unique text, `SYN-001` … `SYN-026` | Stable synthetic identifier, not personal information |
| transaction_date | Date, `YYYY-MM-DD` | Valid calendar date, without a time zone |
| amount | Exact decimal with two decimal places | No thousands separators; a minus sign is allowed; no floating-point arithmetic |
| currency | Three uppercase ASCII letters | The generator emits USD; detection checks syntax only, not ISO 4217 membership or currency conversion. |
| error_ids | Text; IDs separated by `;`, without spaces or duplicates, in the order E01, E02, E03, E04 | Empty means clean; ground-truth metadata, not a business field |

These are logical types: the CSV reader preserves strings so that malformed
values remain intact. The generator uses integer cents. No balances, accounts,
categories, or business rules are assumed. No real personal information is used.

## Catalog and Traceability

`catalog.json` is the canonical catalog of defect IDs, descriptions, affected
columns, detection rules, and all example transaction IDs. Each row includes
`error_ids`, allowing a single small CSV to retain traceability without fragile
line-number joins. Exclude this column from production inputs and predictive
features. Detection rules inspect values independently of this label; the
validator then compares the detected defects with the exact ground-truth labels.
It neither cleans nor discards rows.

| ID | Defect / column | Rule summary | Transaction IDs (CSV line numbers, including the header) |
|---|---|---|---|
| E01 | Missing amount / amount | Empty string | SYN-003, SYN-019, SYN-025 (4, 20, 26) |
| E02 | Invalid date / transaction_date | `date.fromisoformat` raises `ValueError` or `re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", transaction_date)` fails | SYN-007, SYN-023, SYN-025 (8, 24, 26) |
| E03 | Malformed amount / amount | Nonempty value fails the two-decimal-place format | SYN-011, SYN-026 (12, 27) |
| E04 | Malformed currency / currency | Value fails the three-uppercase-ASCII-letter format | SYN-015, SYN-026 (16, 27) |

The amount format rejects leading zeros, such as `01.23`.

Each catalog entry includes `schema_status: "PROVISIONAL — pending confirmation"`.
For E02, `date` means `datetime.date`: the date must be accepted by
`date.fromisoformat` and fully match the stated ASCII pattern. For example,
`20260115` fails the regular expression even if `date.fromisoformat` accepts it;
`2026-02-30` fails calendar validation.

E01 and E03 are mutually exclusive, distinguishing missing values from malformed
ones. The two multi-error cases combine defects in different columns and cover
all four defect types without combining E01 with E03. The original 24
transactions retain their values.

| Multi-error case (CSV line) | Simultaneous mutations | `error_ids` |
|---|---|---|
| SYN-025 (26) | Empty `amount` and `transaction_date=2026-02-30` | `E01;E02` |
| SYN-026 (27) | `amount=12x.50` and `currency=US$` | `E03;E04` |

Occurrences by type: E01=3, E02=3, E03=2, E04=2 (10 defects across 8 rows).

## Reproduce and Validate

From the repository root, using Python 3 and only the standard library:

```sh
python3 data/ofl-015/fixture.py generate
python3 data/ofl-015/fixture.py validate
```

The seed (`15024`), dates, IDs, ordering, and serialization are fixed.
`generate` overwrites only `transactions.csv` beside the script and prints its
SHA-256 digest. Repeated runs produce identical bytes in the same Python
environment. `validate` does not regenerate data: it checks the 26-row count,
column names and order, CSV record structure, IDs, catalog coverage and examples,
canonical labels, and detection rules. It requires clean controls and at least
one multi-error row. Multiple labels are accepted only when their set exactly
matches all detected defects. A failure prints `FAIL` and exits with code 1;
success exits with code 0.

Validation checks the four deliberate defect types, not every possible financial
rule or byte-for-byte integrity: a change to another valid field value may pass.
No network access, services, or third-party dependencies are required.

The self-contained provisional fixture lives in `data/ofl-015/`, following the
repository README's suggested location for datasets and data documentation.
