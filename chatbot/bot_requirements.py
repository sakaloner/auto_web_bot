import os
import re
import openai

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "218d14c3ee3ad7ab734199d125889b23a0acdf5144feaf540abdfa4a22ed3e65"
openai.api_key = os.environ["OPENAI_API_KEY"]
first_prompt = """You will help the user to create an ecommerce webpage:
You need to ask the user for the name of its company, the slogan of its company, and if the user has
products for displaying on its webpage.

You need to save the answears form the users to this information in python dictionaries, Dont tell the user about this dictionary.
After you get all the necessary info from the user you need to output the keywork GENERATING_WEBPAGE
Example:
assistant: Hello how can i help you today?
user: i want to create a webpage for my shoestore
assistant: allright whats the name of your company?
user: the name of my company is ShoeStringMax
assistant: |"company_name": "ShoeStringMax| allright do you want to display products in your webpage?
user: yeah i would like that
assistant: |"diplay_products":True| alrgiht, last thing. Whats your company slogan?
user: the slogan is "We love them shoes!!!"
assistant: |"slogan":"We love them shoes!!!"| all right, we are generating the webpage right now, please
wait. GENERATING_WEBPAGE"""
chat_history = [
  {"role": "system", "content": first_prompt},
]
### parser
def extract_dict(text):
    pattern = r'```python(.*?)```'
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return None

def output_parser(text):
    if "GENERATING_WEBPAGE" in text:
        print('Generate the webpage!!!!!')
        return True
    if "```python" in text:
        text = extract_dict(text)
        print(text)
        return True
    else:
       return False

def talk(chat_history, message, debug=False):
  ## add user message
  chat_history.append({"role":"user","content":message})
  ## get bot response
  res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat_history
  )
  text_res = res.choices[0].message.content
  ## add bot response
  chat_history.append({"role":"assistant","content":text_res})
  if debug:
    print(chat_history)
  return text_res

count = 0
while True:
  if count == 0:
    print("Hello i am an AI assistant here to help you create a beutiful webpage. How can i start helping you today?")
  user_input = input()
  bot_res = talk(chat_history, user_input)
  output_parser(bot_res)
  print(bot_res)
  #print(output_parser)
  count += 1