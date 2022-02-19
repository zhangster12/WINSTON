'''Main file where WINSTON is run'''
from audio import *
from phrase import *
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
            if check_all_phrase(listened_text, ['search', 'wikipedia']):
                wiki_search = listen(source, 'Type your search.\n')

                print(wikipedia.summary(wikipedia.search(wiki_search)[0]))
                input('Enter to continue.\n')

            elif check_all_phrase(listened_text, ['who are you',
                'what does winston stand for',
                'what are you']):

                speak_text('WINSTON is Wise Intelligent Nebulous Sophisticated Technical Operating System.')

            elif 'excel' in listened_text:
                os.system('start excel.exe')

            elif check_all_phrase(listened_text, ['exit', 'goodbye', 'quit', 'go away', 'bye', 'cancel']):
                speak_text('Goodbye.')
                break

            elif 'help' in listened_text:
                print('Excel: Open Excel')

            elif 'clear' in listened_text:
                os.system('cls')

            # Time related
            elif check_all_phrase(listened_text, time_info.time_list):
                speak_text(time_info.check_phrase_time(listened_text))

            else:
                speak_text(chatbot.ask(listened_text))

    except KeyboardInterrupt:
        speak_text('Goodbye.')
        break