import openai
import os
from prompts import dashboard_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_dashboard(df):
    sample_summary = str(df.describe(include='all'))[:2000]
    prompt = dashboard_prompt.format(data_summary=sample_summary)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a dashboard planner bot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]