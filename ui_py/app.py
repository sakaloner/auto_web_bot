import json 
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError
import os
from dotenv import load_dotenv 
import elbot 


app = Flask(__name__)
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
#=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
#os.environ["OPENAI_API_KEY"] = "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"
#OPENAI_API_KEY="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"

#openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = "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"
ai_key = openai.api_key
talk = elbot.bot()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
 
    try:
        response = talk(user_input)
        content = response
    except RateLimitError:
        content = "Calma, intentalo mais tarde \n"
    

    return jsonify(content=content)



##########################################################


if __name__ == '__main__':
    app.run(debug=True)

