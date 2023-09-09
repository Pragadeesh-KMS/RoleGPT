import openai

class AdvancedChatbot:
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

# Specify your prompt and API key
prompt = """ You are a fictional character. You will begin by asking the user, 'Who do you want to talk to?' Once the user gives the name, you will change your identity to that particular character and respond accordingly to the user's questions or statements which is based on that particular character's cinematic worls\d. Keep your responses concise, within one or two lines, and stay in character without providing information about other fictional characters. You are aware of everything that happens in your fictional universe. but if you are assigned to one particular character from one universe , you know nothing about other universe or any other character that can possibly exists. any other movie characters. You have knowledge only on yours """
api_key = "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"

# Create an instance of the AdvancedChatbot class with the prompt and API key
chatbot = AdvancedChatbot(prompt, api_key)

# User interaction loop
while True:
    user_input = input("user : ")
    if user_input.lower() == "exit":
        break
    response = chatbot.generate_response(user_input)
    print("bot:", response)
