"""The merchant payments API."""
from rules.loader import approval_limit


def create_payment(db, merchant_id, amount_eur, card_token):
    status = "pending_approval" if needs_manual_approval(amount_eur) else "authorised"
    return db.insert("payments", {"merchant_id": merchant_id, "amount_eur": amount_eur,
                                  "card_token": card_token, "status": status})


def needs_manual_approval(amount_eur):
    return amount_eur > approval_limit()


def capture_payment(db, payment_id):
    db.update("payments", payment_id, {"status": "captured"})
