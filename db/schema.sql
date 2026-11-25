CREATE TABLE cust_master (
    cust_id      VARCHAR(20) PRIMARY KEY,
    legal_name   VARCHAR(200) NOT NULL,
    settle_iban  VARCHAR(34) NOT NULL
);

CREATE TABLE payments (
    id           BIGINT PRIMARY KEY,
    merchant_id  VARCHAR(20) REFERENCES cust_master (cust_id),
    amount_eur   NUMERIC(12, 2) NOT NULL,
    card_token   VARCHAR(64) NOT NULL,
    status       VARCHAR(20) NOT NULL
);

CREATE TABLE ledger_entries (
    merchant_id   VARCHAR(20) REFERENCES cust_master (cust_id),
    iban          VARCHAR(34) NOT NULL,
    business_date DATE NOT NULL,
    amount_eur    NUMERIC(14, 2) NOT NULL,
    PRIMARY KEY (merchant_id, business_date)
);
