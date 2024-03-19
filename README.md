# Usage


# Commands
```
pip freeze > requirements.txt
docker compose rm -fsv flask_api db
docker compose up --build
```

# Prompt template
### Task
Generate a SQL query to answer [QUESTION]{user_question}[/QUESTION]

### Database Schema
The query will run on a database with the following schema:
{table_metadata_string_DDL_statements}

### Answer
Given the database schema, here is the SQL query that [QUESTION]{user_question}[/QUESTION]
[SQL]

user_question: 
get the first row of table
table_metadata_string_DDL_statements:
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

