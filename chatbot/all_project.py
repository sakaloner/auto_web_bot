from utils.funcs import talk, parser_code, parser_code
import os

# Fake output requirements
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
#### se debe eliminar la variable file_contents del prompt mientras que no se vaya a leer archivo
file_contents = None
initial_prompt = f"""Use this data: {user_requirements} to create the "company_name", "slogan",
 "display_products" and "products" values in an svelte page for a ecommerce store. This is the
 current value of the page, and you need to output the updated code. Output only the code. {file_contents}"""

promp_list = f" I want to create an online ecommerce store webpage. I am using svelte. Tell me what files do you need to create to create my webpage.Dont output code. Just output a list of the .svelte files the webstore would need. This is the data for my webpage: {user_requirements} {file_contents}"
def make_project(files_list):
  # rearange files_list to put the App.svelte file at the end
  files_list.remove('App.svelte')
  files_list.append('App.svelte')
  for match in files_list:
    prompt = f"create a .svelte file for this component: {match}"
    res = talk(prompt)
    print("res", res)
    res_parsed = parser_code(res)
    os.makedirs('tmp', exist_ok=True)
    with open(f"tmp/{match}", "w") as file:
      file.write(res_parsed)