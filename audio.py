import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()

def speak_text(text):
    '''Speaks a line of text'''

    engine = pyttsx3.init()
    print('WINSTON: ' + str(text))
    engine.say(text)
    engine.runAndWait()

def listen(source, message):
    print('Listening...')
    audio = listener.listen(source)

    try:
        listened_text = listener.recognize_google(audio).lower()
        print(listened_text.capitalize())
    except sr.UnknownValueError as e:
        listened_text = input(message)
    
    return listened_text