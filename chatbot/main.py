import openai
import os
from dotenv import load_dotenv 
from all_project import *
from only_comp import *

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


if __name__ == "__main__":
  make_comp()
  #make_proyect(l1)
