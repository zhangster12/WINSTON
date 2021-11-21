from decouple import config
import openai

openai.api_key = config('OPENAI_API_KEY')

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

        answer = response.choices[0].text.strip()
        self.append_to_chatlog(question.capitalize(), answer)
        return answer

    def append_to_chatlog(self, question, answer):
        self.chat_log = f'{self.chat_log}Human: {question}\nAI: {answer}\n'