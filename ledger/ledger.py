"""Writes settlement rows to the ledger."""


def post_settlement(db, merchant_id, account, business_date, total_eur):
    db.insert("ledger_entries", {"merchant_id": merchant_id, "iban": account,
                                 "business_date": business_date, "amount_eur": total_eur})


def find_entry(db, merchant_id, business_date):
    return db.select_one("ledger_entries", merchant_id=merchant_id, business_date=business_date)
