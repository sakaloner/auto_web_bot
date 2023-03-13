## openai code-davinci
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt2 = """
<!-- Create a web page with the title 'Vegan Fast Food'.
Use Tailwind CSS to style the page. -->
<!DOCTYPE html>
"""

prompt3 = """
<!-- Create a landing page for a crypto currency exchange with html -->
<!DOCTYPE html>
"""

response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=prompt3,
    temperature=0.3,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response.choices[0].text)
with open("../index.html", "w") as f:
    full_text = response.choices[0].text
    f.write(full_text)

newPrompt = response.choices[0].text + prompt3

response2 = openai.Completion.create(
    engine="code-davinci-002",
    prompt=newPrompt,
    temperature=0.3,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response2.choices[0].text)
with open("../styles.css", "w") as f:
    full_text = response2.choices[0].text
    f.write(full_text)