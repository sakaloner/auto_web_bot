import openai
import re

def talk(prompt, talk_history=[]):
  talk_history.append({"role": "user", "content": prompt})
  res_raw = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=talk_history,
  )

  res = res_raw.choices[0].message.content
  return res


def parser_list_files(text):
  # search for files with the .svlete extension
  pattern = r"(\w+\.svelte)"
  # find all matches
  matches = re.findall(pattern, text)
  # print(matches)
  return matches


def parser_code(res):
  pattern = r"```(.*?)```"
  # find the match
  match = re.search(pattern, res, re.DOTALL)
  # erase the html part if it exists on the match
  match = re.sub(r"html", "", match.group(1))
  return match