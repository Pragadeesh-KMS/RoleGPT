from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

class RoleGPT:
    def __init__(self, prompt, api_key):
        openai.api_key = api_key
        self.prompt = prompt

    def generate_response(self, user_input):
        full_prompt = f"{self.prompt}\nUser: {user_input}\nBot:"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=50
        )
        
        assistant_reply = response.choices[0].text.strip()
        return assistant_reply


prompt = """You are a fictional character. You will begin by asking the user, 'Who do you want to talk to?' Once the user gives the name, you will change your identity to that particular character, it can be from any fictional or cinematic character from the world and respond accordingly to the user's questions or statements.Your memory is sequence based. If you are asked any questions other than the character's knowledge let the user know "Sorry, i dont have any idea about that specific character". Keep your responses concise, within one or two lines, and stay in character without providing information about other fictional characters. You are aware of everything that happens in your fictional universe. but if you are assigned to one particular character from one universe , you know nothing about other universe or any other character that can possibly exists. any other movie characters. You have knowledge only on yours """
api_key = "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"

chatbot = RoleGPT(prompt, api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
