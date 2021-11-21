import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

class chatbot:
    chat_log = 'Human: Hello, who are you?\nAI: I am doing great. How can I help you today?\n'

    def ask(self, question):
        prompt = f'{self.chat_log}Human: {question}\nAI: '
        response = openai.Completion.create(
            engine = "davinci",
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0.7,
            presence_penalty = 0.6,
            best_of = 1,
            stop = ['\nHuman']
        )
        self.chat_log = f'{self.chat_log}{prompt}{response.choices[0].text.strip()}'
        return response.choices[0].text.strip()