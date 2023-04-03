import openai
import json

openai.api_key = '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'

prompt = "HelloWorld! How are you?"

response = openai.Completation.create(
    engine = "text-davinci-002"
    prompt = prompt,
    max_tokens = 60
)

print(response.chaices[0].text)

