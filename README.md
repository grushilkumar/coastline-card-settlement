# Coastline Card Settlement

Coastline Bank settles card payments for its merchants. This repository holds the payments API,
the approval rules, the nightly settlement job, the bank statement reconciliation and the ledger.

## How a payment moves

1. A merchant calls `create_payment` in `api/payments_api.py`.
2. A payment at or under `APPROVAL_LIMIT` in `rules/limits.yaml` is authorised at once.
   A larger one waits for a person (`needs_manual_approval`).
3. `capture_payment` marks the payment captured.

## Nightly settlement

`run_nightly_settlement` in `batch/settle_nightly.py` runs at 01:30. It reads captured payments,
groups them by merchant and writes one row per merchant to `ledger_entries` through `post_settlement`.
It reads the `cust_master` table only to find each merchant's settlement account.
It never changes customer records.

## Reconciliation

Each morning the bank sends a statement file to `inbound/`. `reconcile_statement` in
`reconcile/reconcile.py` matches each statement line to a ledger entry. The matcher for a line
is chosen by its record type (`match_card`, `match_refund`, `match_fee`).

## Data

Tables are in `db/schema.sql`.
