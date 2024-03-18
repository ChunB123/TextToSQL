def generate_text_to_sql_prompt(question):
    prompt = """Generate a SQL query to answer [QUESTION]{user_question}[/QUESTION]

    The query will run on a database with the following schema:
    {table_metadata_string}

    Given the database schema, here is the SQL query that [QUESTION]{user_question}[/QUESTION]"""

    table_metadata_string = """CREATE TABLE IF NOT EXISTS tsla_stock_data (
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
    );"""
    prompt = prompt.format(
        user_question=question, table_metadata_string=table_metadata_string
    )
    return prompt