from flask_app.models.chatgpt import text_to_sql_gpt3, sql_is_query_or_not_gpt3
from flask_app.models.model_utils import generate_text_to_sql_prompt

def text_to_sql(text_query: str) -> str:
    prompt = generate_text_to_sql_prompt(text_query)
    gpt_output = text_to_sql_gpt3(prompt, max_tokens=100)
    return gpt_output

def sql_is_query_or_not(sql_query: str) -> bool:
    prompt = "Does this SQL is SQL SELECT Statement or not?" + sql_query
    gpt_output = sql_is_query_or_not_gpt3(prompt, max_tokens=100)
    return gpt_output
