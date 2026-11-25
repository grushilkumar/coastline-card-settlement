"""Nightly settlement. Scheduled at 01:30 by cron: 30 1 * * *"""
from ledger.ledger import post_settlement

BATCH_SIZE = 5000


def run_nightly_settlement(db, business_date):
    payments = db.select("payments", status="captured", limit=BATCH_SIZE)
    for merchant_id, total in group_by_merchant(payments).items():
        account = settlement_account(db, merchant_id)
        post_settlement(db, merchant_id, account, business_date, total)
    db.update_many("payments", [p["id"] for p in payments], {"status": "settled"})


def group_by_merchant(payments):
    totals = {}
    for p in payments:
        totals[p["merchant_id"]] = totals.get(p["merchant_id"], 0) + p["amount_eur"]
    return totals


def settlement_account(db, merchant_id):
    return db.select_one("cust_master", cust_id=merchant_id)["settle_iban"]
