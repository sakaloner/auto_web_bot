import openai
import os
from dotenv import load_dotenv 
from all_project import *
from only_comp import *

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY


if __name__ == "__main__":
  make_comp()
