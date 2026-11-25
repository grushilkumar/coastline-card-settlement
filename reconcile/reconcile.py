"""Matches the bank's morning statement against the ledger."""
from ledger.ledger import find_entry


def reconcile_statement(db, lines):
    unmatched = []
    for line in lines:
        matcher = globals()["match_" + line["record_type"]]
        if not matcher(db, line):
            unmatched.append(line)
    return unmatched


def match_card(db, line):
    entry = find_entry(db, line["merchant_id"], line["business_date"])
    return entry is not None and entry["amount_eur"] == line["amount_eur"]


def match_refund(db, line):
    return find_entry(db, line["merchant_id"], line["business_date"]) is not None


def match_fee(db, line):
    return line["amount_eur"] < 0
