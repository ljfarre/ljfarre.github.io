import openai
# openai.api_key = "YOUR_API_KEY"
os.environ["openai_api_key"] = "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"
os.getenv('openai_api_key')
openai.api_key = os.getenv('openai_api_key')

def generate_text(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text