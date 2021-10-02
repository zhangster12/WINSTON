#Wise Intelligent Nebulous Sophisticated Technical Operating System
import speech_recognition as sr
import os, pyttsx3

os.system('cls')

listener = sr.Recognizer()

# Speaks a line of text
def speak_text(text):
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Listening...')
        audio = listener.listen(source)
        text = listener.recognize_google(audio)
        speak_text(text)

except:
    speak_text('The microphone\'s not working.')
    pass