import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def text_to_sql_gpt3(prompt, max_tokens=512):
    add_on = "Return only the SQL itself in the completion."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=max_tokens,
        messages=[
            {"role": "system",
             "content": "You are a data engineer, skilled in translating natural language to SQL for PostgreSQL database"},
            {"role": "user", "content": prompt + add_on}
        ]
    )
    output = completion.choices[0].message.content
    cleaned_code = output.replace("```sql\n", "").replace("\n```", "")
    return cleaned_code

def sql_is_query_or_not_gpt3(prompt, max_tokens=5):
    add_on = "Return only YES or NO in the completion."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=max_tokens,
        messages=[
            {"role": "system",
             "content": "You are a data engineer, skilled in recognizing SELECT SQL"},
            {"role": "user", "content": prompt + add_on}
        ]
    )
    print(completion.choices[0].message.content)
    return True if completion.choices[0].message.content.__contains__("YES") else False
