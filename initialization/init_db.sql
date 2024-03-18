-- noinspection SqlNoDataSourceInspectionForFile
CREATE TABLE IF NOT EXISTS tsla_stock_data (
    date DATE PRIMARY KEY,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT,
    rsi_7 NUMERIC,
    rsi_14 NUMERIC,
    cci_7 NUMERIC,
    cci_14 NUMERIC,
    sma_50 NUMERIC,
    ema_50 NUMERIC,
    sma_100 NUMERIC,
    ema_100 NUMERIC,
    macd NUMERIC,
    bollinger NUMERIC,
    TrueRange NUMERIC,
    atr_7 NUMERIC,
    atr_14 NUMERIC,
    next_day_close NUMERIC
);