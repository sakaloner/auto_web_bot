import openai
import os
import re

# Set OpenAI API key
openai.api_key = "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"


# Output requirements
user_requirements = {
    "company_name": "Rancherito",
    "slogan": "La mejor sazon antioquena",
    "display_products": True,
    "products": {
        "Bandeja paisa": 20,
        "Claro con mazamorra": 5,
        "Carne asada": 30,
        "Chicharrón ahumado gigante": 35        
    }
}

with open("./App.svelte", "r") as file:
    # Read the file contents into a string
    file_contents = file.read()

#print(type(file_contents))
#print(file_contents)
'''
# Modify the file contents using GPT
new_contents = modify_text_with_gpt(file_contents)

# Open the file for writing
with open("output.txt", "w") as file:
    # Write the modified contents to the file
    file.write(new_contents)

# Remove original file
os.remove("input.txt")

# Rename output file to original file name
os.rename("output.txt", "input.txt")
'''


# Modify file AI


promptInicial = f"""Use this data: {user_requirements} to create the "company_name", "slogan",
 "display_products" and "products" values in an svelte page for a ecommerce store. This is the
 current value of the page, and you need to output the updated code. Output only the code. {file_contents}"""

prompt2 = f" I want to create an online ecommerce store webpage. I am using svelte. Tell me what files do you need to create to create my webpage.Dont output code. Just output a list of the .svelte files the webstore would need. This is the data for my webpage: {user_requirements} {file_contents}"
# print(f'Prompt: {prompt}')
# 
# response = openai.completion.create(
#     # engine="text-davinci-003",
#     engine='gpt-4',
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )
# res = response.choices[0].text.strip()
# print(f"res:", res)

talk_history = [
  {"role": "system", "content": "You are a frontend coding assistant."},
]
def talk(prompt):
  talk_history.append({"role": "user", "content": prompt})
  res_raw = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=talk_history,
  )

  res = res_raw.choices[0].message.content
  return res

# res= talk(prompt2)
# print(res)

def parser_list(text):
  # search for files with the .svlete extension
  pattern = r"(\w+\.svelte)"
  # find all matches
  matches = re.findall(pattern, text)
  # print(matches)
  return matches

# matches = parser_list(res)

def parser_files(res):
  # create a pattern to match the substring that cointains code as html ... 
  pattern = r"```(.*?)```"
  # find the match
  match = re.search(pattern, res, re.DOTALL)
  # erase the html part if it exists on the match
  match = re.sub(r"html", "", match.group(1))
  # print(match)
  # print(match.group(1))
  return match

def make_files(files_list):
  # rearange files_list to put the App.svelte file at the end
  files_list.remove('App.svelte')
  files_list.append('App.svelte')
  for match in files_list:
    prompt3 = f"create a .svelte file for this component: {match}"
    res = talk(prompt3)
    print("res", res)
    res_parsed = parser_files(res)
    os.makedirs('web_files', exist_ok=True)
    with open(f"tmp/{match}", "w") as file:
      file.write(res_parsed)

def create_one_comp():
  p = """Show me the code for product.svelte file, it is the component for adding a product to a cart for an ecommerce store
  style this component with beutiful tailwind code"""
  res = talk(p)
  print(res)
  code = parser_files(res)
  print(code)
  with open("ecom/src/lib/compon.svelte", "w") as file:
    file.write(code)


create_one_comp()
#artificial_files = 
# make_files(matches)

