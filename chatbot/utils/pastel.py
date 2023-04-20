import openai
import json

# Set up OpenAI API credentials
openai.api_key = "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"

# Define prompt for eliciting requirements
prompt = (
    "Hello! I'm here to help you elicit your requirements. "
    "What features would you like in your new product? Please describe them in as much detail as possible."
)

# Define function to generate response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    return message

# Start chat with user
while True:
    user_input = input("User: ")
    prompt += "\nUser: " + user_input
    response = generate_response(prompt)
    prompt += "\nBot: " + response
    print("Bot:", response)

    # Check if user has provided enough information to stop the loop
    if "webpage" in response:
        break

