from utils.funcs import talk, parser_code, parser_code

def make_comp():
  p = """Show me the code for product.svelte file, it is the component for adding a product to a cart for an ecommerce store
  style this component with beutiful tailwind code"""
  res = talk(p)
  print(res)
  code = parser_code(res)
  print(code)
  with open("ecom/src/lib/compon.svelte", "w") as file:
    file.write(code)