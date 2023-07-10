import openai
from dotenv import load_dotenv
import os

class OpenAIChat:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_KEY")
        self.messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
      
    def chat_with_gpt3(self, prompt):
        self.messages.append({'role': 'user', 'content': prompt})

        # Calling the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages
        )
        self.messages.append({
            'role': 'assistant',
            'content': response.choices[0]['message']['content']
        })
        return response.choices[0]['message']['content']
    
    def remove_message(self, message_content):
        self.messages = [msg for msg in self.messages if msg['content'] != message_content]

    def show_chat_history(self):
        for message in self.messages:
            print(f"{message['role']}: {message['content']}")  