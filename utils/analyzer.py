import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_security(text):
    prompt = f"""
    You are a cybersecurity expert.

    Analyze the following input for:
    1. Security vulnerabilities
    2. Prompt injection risks (if any)
    3. Unsafe coding practices
    4. Risk level (Low / Medium / High)
    5. Suggested fixes

    Provide a clear and structured response.

    Input:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']
