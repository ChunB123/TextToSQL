from openai import OpenAI

client = OpenAI(api_key="")

def gpt3_output(prompt, max_tokens=10):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=max_tokens,
        messages=[
            # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print("Finish")
