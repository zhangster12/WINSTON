from chatbot import chatbot
import os
import pyttsx3
import speech_recognition as sr
from time_info import Time

os.system('cls')

# Create class instance
listener = sr.Recognizer()
chatbot = chatbot()
time_info = Time()


# Speaks a line of text
def speak_text(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()


while True:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = listener.listen(source)
            text = listener.recognize_google(audio).lower()
            print(text.capitalize())

            if 'what does winston stand for' in text:
                speak_text('WINSTON is Wise Intelligent Nebulous \
                    Sophisticated Technical Operating System.')
            elif 'excel' in text:
                os.system('start excel.exe')
            elif any(phrase in text for phrase in ['exit', 'goodbye', 'quit']):
                break
            elif 'help' in text:
                print('Excel: Open Excel')
            elif 'month' in text:
                speak_text(time_info.get_month())
            elif 'weekday' in text:
                speak_text(time_info.get_weekday())
            else:
                speak_text(chatbot.ask(text))

    except KeyboardInterrupt:
        speak_text('Goodbye.')
        break

    except Exception:
        speak_text('The microphone\'s not working.')
        pass
