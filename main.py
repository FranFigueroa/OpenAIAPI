import openai
import json

openai.api_key = "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"

prompt = "Hola, ¿cómo estás?"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=60
)

print(response.choices[0].text)

