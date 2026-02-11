import openai
from utils.prompt_builder import build_prompt

openai.api_key = "YOUR_API_KEY"

def generate_explanation(result):
    prompt = build_prompt(result)

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You explain AI decisions clearly."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"]
