'''Main file where WINSTON is run'''
from audio import *
from chatbot import Chatbot
from time_info import Time
import os, wikipedia
import speech_recognition as sr

os.system('cls')

# Create class instance
chatbot = Chatbot()
time_info = Time()

while True:
    try:
        with sr.Microphone() as source:
            listened_text = listen(source, 'Type your message.\n')

            # Wikipedia search
            if any(phrase in listened_text for phrase in ['search', 'wikipedia']):
                wiki_search = listen(source, 'Type your search.\n')

                print(wikipedia.summary(wikipedia.search(wiki_search)[0]))
                input('Enter to continue.\n')

            elif any(phrase in listened_text for phrase in ['who are you',
                'what does winston stand for']):

                speak_text('WINSTON is Wise Intelligent Nebulous Sophisticated Technical Operating System.')

            elif 'excel' in listened_text:
                os.system('start excel.exe')

            elif any(phrase in listened_text for phrase in ['exit', 'goodbye', 'quit', 'go away', 'bye']):
                speak_text('Goodbye.')
                break

            elif 'help' in listened_text:
                print('Excel: Open Excel')

            elif 'clear' in listened_text:
                os.system('cls')

            # Time related
            elif any(phrase in listened_text for phrase in ['month', 'day of week', 'time', 'date', 'year']):
                speak_text(time_info.check_phrase_time(listened_text))

            else:
                speak_text(chatbot.ask(listened_text))

    except KeyboardInterrupt:
        speak_text('Goodbye.')
        break