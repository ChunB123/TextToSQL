# TextToSQL Application
Model: GPT3.5

Data: initialization/tsla_2014_2023.csv

## Set up
### Data Flow Chart
```
Receive HTTP call
        |
        v
  Flask server
        |
        v
Text_to_SQL (OPENAI)
        |
        v
If_SQL_is_SELECT (OPENAI)
        |
        v
     Query DB
        |
        v
Return JSON Object
```

### Populating DB
Scripts inside the initialization folder will be executed during the database's startup phase.

## Test
### Procedure
1. Create .env file at root directory with content "OPENAI_API_KEY=your_api_key" (Accessing GPT 3.5 is required).
2. Spin up api and db containers.
```bash
docker compose up --build
```
3. Test API.
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"query": "What date had the highest trading volume, and what was the closing price on that day?"}' http://localhost:5000/query
```

### Test cases
1. SELECT SQL generation 1
```json
{"query": "What date had the highest trading volume, and what was the closing price on that day?"}
```
```json
{
    "result": [
        [
            "Tue, 04 Feb 2020 00:00:00 GMT",
            "59.137333"
        ]
    ],
    "sql_query": "SELECT date, close\nFROM tsla_stock_data\nWHERE volume = (SELECT MAX(volume) FROM tsla_stock_data);",
    "status": "success"
}

```
2. SELECT SQL generation 2
```json
{"query": "On how many days does the closing price exceed both the SMA_50 and EMA_50, indicating a potentially bullish signal?"}
```
```json
{
    "result": [
        [
            1321
        ]
    ],
    "sql_query": "SELECT COUNT(*) AS bullish_days\nFROM tsla_stock_data\nWHERE close > sma_50 AND close > ema_50;",
    "status": "success"
}
```
3. Create table SQL generation (Forbidden)
```json
{"query": "How many birds are there from the table birds_examples?"}
```
```json 
{
    "internal_error": "relation \"birds_examples\" does not exist\nLINE 1: SELECT COUNT(*) FROM birds_examples;\n                             ^\n",
    "message": "psycopg2.DatabaseError",
    "sql_query": "SELECT COUNT(*) FROM birds_examples;",
    "status": "error"
}
```
4. Delete table SQL generation (Fobidden)
```json
{"query": "Delete this table"}
```
```json
{
    "message": "Query is not a SELECT SQL",
    "sql_query": "DROP TABLE IF EXISTS tsla_stock_data;",
    "status": "error"
}
```
        
        

## Commands
```
pip freeze > requirements.txt
docker compose rm -fsv flask_api db
docker compose up --build
docker exec ID -it /bin/bash

git restore --staged .
```

## Prompt template for text_to_SQL
Generate a SQL query to answer [QUESTION]{user_question}[/QUESTION]

The query will run on a database with the following schema:
{table_metadata_string_DDL_statements}

Given the database schema, here is the SQL query that [QUESTION]{user_question}[/QUESTION]
[SQL]