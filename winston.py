'''Main file where WINSTON is run'''
from chatbot import Chatbot
from time_info import Time
import os, pyttsx3
import speech_recognition as sr

os.system('cls')

# Create class instance
listener = sr.Recognizer()
chatbot = Chatbot()
time_info = Time()

def speak_text(text):
    '''Speaks a line of text'''

    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = listener.listen(source)
            listened_text = listener.recognize_google(audio).lower()
            print(listened_text.capitalize())

            if 'what does winston stand for' in listened_text:
                speak_text('WINSTON is Wise Intelligent Nebulous Sophisticated Technical Operating System.')
            elif 'excel' in listened_text:
                os.system('start excel.exe')
            elif any(phrase in listened_text for phrase in ['exit', 'goodbye', 'quit']):
                break
            elif 'help' in listened_text:
                print('Excel: Open Excel')
            elif 'month' in listened_text:
                speak_text(time_info.get_month())
            elif 'day of week' in listened_text:
                speak_text(time_info.get_day_of_week())
            elif 'what time is it' in listened_text:
                speak_text(time_info.get_current_time())
            elif 'date' in listened_text:
                speak_text(time_info.get_date())
            else:
                speak_text(chatbot.ask(listened_text))

    except KeyboardInterrupt:
        speak_text('Goodbye.')
        break

    except Exception:
        speak_text('The microphone\'s not working.')
