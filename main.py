## openai code-davinci
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
<!-- Create a landing page for a crypto currency exchange with html -->
<!DOCTYPE html>
"""
responseChat = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)


print(response.choices[0].text)
print(responseChat.choices[0].message.content)
## Guardar respuesta en un archivo
with open("../index.html", "w") as f:
    full_text = response.choices[0].text
    f.write(full_text)
# 