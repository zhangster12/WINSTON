import os, pyttsx3
import speech_recognition as sr

os.system('cls')

listener = sr.Recognizer()

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
            if 'what does winston stand for' in text:
                speak_text('WINSTON is Wise Intelligent Nebulous Sophisticated Technical Operating System.')
            speak_text(text)

    except:
        speak_text('The microphone\'s not working.')
        pass