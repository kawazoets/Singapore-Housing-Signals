"""
Singapore Housing Signals
Public analysis pipeline used for the Version 1.1 workbook.

Purpose
-------
This script shows the core data-processing steps behind the project:

Raw Excel data
    -> quarterly alignment
    -> QoQ verification
    -> policy-event matching
    -> integrated signal table
    -> policy-reaction analysis

It intentionally focuses on the analytical pipeline rather than reproducing
every formatting detail of the published workbook.

Required input files
--------------------
HDB_Resale_Price.xlsx
Private_Property_Price.xlsx
HDB_Transaction_Volume.xlsx
Private Transaction Volume.xlsx
Policy_Timeline.xlsx
"""

from datetime import datetime, timedelta
from pathlib import Path

from artifact_tool import Blob, SpreadsheetFile


BASE = Path(".")
FILES = {
    "hdb_price": BASE / "HDB_Resale_Price.xlsx",
    "private_price": BASE / "Private_Property_Price.xlsx",
    "hdb_volume": BASE / "HDB_Transaction_Volume.xlsx",
    "private_volume": BASE / "Private Transaction Volume.xlsx",
    "policy": BASE / "Policy_Timeline.xlsx",
}


def load_first_sheet(path: Path, cell_range: str):
    wb = SpreadsheetFile.import_xlsx(Blob.load(str(path)))
    sh = wb.worksheets.get_item_at(0)
    return sh.get_range(cell_range).values


def nonblank_rows(values):
    return [r for r in values[1:] if r and r[0] not in (None, "")]


def excel_serial_to_date(serial):
    # Excel's standard 1900 date system.
    return datetime(1899, 12, 30) + timedelta(days=float(serial))


def quarter_from_date(dt):
    quarter = (dt.month - 1) // 3 + 1
    return f"{dt.year}-Q{quarter}"


def quarter_number(q):
    year = int(q[:4])
    quarter = int(q[-1])
    return year * 4 + quarter


def validate_qoq(rows, value_col=1, qoq_col=2, tolerance=0.0015):
    """
    Recalculate QoQ from the underlying level series and compare it
    with the QoQ values already present in the source workbook.
    """
    mismatches = []

    for i in range(1, len(rows)):
        previous_value = rows[i - 1][value_col]
        current_value = rows[i][value_col]
        supplied_qoq = rows[i][qoq_col]

        if previous_value in (None, 0) or current_value is None or supplied_qoq is None:
            continue

        calculated_qoq = current_value / previous_value - 1

        if abs(calculated_qoq - supplied_qoq) > tolerance:
            mismatches.append(
                {
                    "quarter": rows[i][0],
                    "supplied": supplied_qoq,
                    "calculated": calculated_qoq,
                }
            )

    return mismatches


def cumulative_change(values):
    if not values:
        return None

    result = 1.0
    for value in values:
        result *= 1 + value
    return result - 1


def prior_quarters(rows, event_quarter, n=4):
    event_no = quarter_number(event_quarter)
    prior = [r for r in rows if quarter_number(r[0]) < event_no]
    return prior[-n:]


# ------------------------------------------------------------------
# 1. Load the source data
# ------------------------------------------------------------------

hdb_price = nonblank_rows(load_first_sheet(FILES["hdb_price"], "A1:F103"))
private_price = nonblank_rows(load_first_sheet(FILES["private_price"], "A1:F103"))
hdb_volume = nonblank_rows(load_first_sheet(FILES["hdb_volume"], "A1:F102"))
private_volume = nonblank_rows(load_first_sheet(FILES["private_volume"], "A1:F103"))
policy_rows = nonblank_rows(load_first_sheet(FILES["policy"], "A1:F20"))


# ------------------------------------------------------------------
# 2. Verify the supplied QoQ fields
# ------------------------------------------------------------------

verification = {
    "HDB Price QoQ": validate_qoq(hdb_price),
    "Private Price QoQ": validate_qoq(private_price),
    "HDB Volume QoQ": validate_qoq(hdb_volume),
    "Private Volume QoQ": validate_qoq(private_volume),
}

print("\nQoQ verification")
print("----------------")
for label, mismatches in verification.items():
    print(f"{label}: {len(mismatches)} mismatches")


# ------------------------------------------------------------------
# 3. Convert policy dates to the same quarterly time axis
# ------------------------------------------------------------------

policy_events = []

for row in policy_rows:
    date = excel_serial_to_date(row[0])
    policy_events.append(
        {
            "date": date,
            "quarter": quarter_from_date(date),
            "policy": row[1],
            "category": row[2],
            "description": row[3],
            "source": row[4],
            "direction": (
                "Easing"
                if row[2] == "Policy Normalisation"
                else "Tightening"
            ),
        }
    )


# ------------------------------------------------------------------
# 4. Build one integrated quarterly signal table
# ------------------------------------------------------------------

hdb_price_map = {r[0]: r for r in hdb_price}
private_price_map = {r[0]: r for r in private_price}
hdb_volume_map = {r[0]: r for r in hdb_volume}
private_volume_map = {r[0]: r for r in private_volume}

policy_by_quarter = {}
for event in policy_events:
    policy_by_quarter.setdefault(event["quarter"], []).append(event)

quarters = [r[0] for r in hdb_price]

signals = []

for quarter in quarters:
    hp = hdb_price_map.get(quarter)
    pp = private_price_map.get(quarter)
    hv = hdb_volume_map.get(quarter)
    pv = private_volume_map.get(quarter)
    policies = policy_by_quarter.get(quarter, [])

    signals.append(
        {
            "quarter": quarter,
            "hdb_price_index": hp[1] if hp else None,
            "hdb_price_qoq": hp[2] if hp else None,
            "private_price_index": pp[1] if pp else None,
            "private_price_qoq": pp[2] if pp else None,
            "hdb_transaction_volume": hv[1] if hv else None,
            "hdb_volume_qoq": hv[2] if hv else None,
            "private_transaction_volume": pv[1] if pv else None,
            "private_volume_qoq": pv[2] if pv else None,
            "policy_events": [p["policy"] for p in policies],
        }
    )


# ------------------------------------------------------------------
# 5. Test the preliminary policy-reaction hypothesis
# ------------------------------------------------------------------
# For every policy event, calculate the cumulative movement during
# the four quarters immediately preceding the intervention.
#
# This is the step used to investigate whether Government action
# appears to line up with:
#
#   Price Momentum x Persistence x Market Segment
#
# with Transaction Volume used as a supporting heat signal.
# ------------------------------------------------------------------

print("\nPolicy events: previous four quarters")
print("-------------------------------------")

for event in policy_events:
    event_quarter = event["quarter"]

    hp4 = prior_quarters(hdb_price, event_quarter, 4)
    pp4 = prior_quarters(private_price, event_quarter, 4)
    hv4 = prior_quarters(hdb_volume, event_quarter, 4)
    pv4 = prior_quarters(private_volume, event_quarter, 4)

    hdb_price_change = cumulative_change(
        [r[2] for r in hp4 if r[2] is not None]
    )
    private_price_change = cumulative_change(
        [r[2] for r in pp4 if r[2] is not None]
    )
    hdb_volume_change = cumulative_change(
        [r[2] for r in hv4 if r[2] is not None]
    )
    private_volume_change = cumulative_change(
        [r[2] for r in pv4 if r[2] is not None]
    )

    def pct(value):
        return "n/a" if value is None else f"{value * 100:.1f}%"

    print(
        f"{event_quarter} | {event['policy']}\n"
        f"  HDB price 4Q:      {pct(hdb_price_change)}\n"
        f"  Private price 4Q:  {pct(private_price_change)}\n"
        f"  HDB volume 4Q:     {pct(hdb_volume_change)}\n"
        f"  Private volume 4Q: {pct(private_volume_change)}\n"
    )


# ------------------------------------------------------------------
# 6. Core interpretation used in Singapore Housing Signals V1.1
# ------------------------------------------------------------------

print(
    "\nWorking framework\n"
    "-----------------\n"
    "Market Signals:\n"
    "  Price Momentum x Persistence x Market Segment\n"
    "  + Transaction Volume as a confirmation / heat signal\n\n"
    "Government Response:\n"
    "  Demand-side: ABSD / SSD / TDSR / LTV / wait-out rules\n"
    "  Supply-side: BTO / GLS / private-land recycling\n\n"
    "Next question:\n"
    "  After Government intervention, where does the next bottleneck move?\n"
)
