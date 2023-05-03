import json 
from flask import Flask, render_template, request, jsonify
from openai.error import RateLimitError
import elbot 




app = Flask(__name__)


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

