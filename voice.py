# import speech_recognition as sr
# import pyttsx3

# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         audio = r.listen(source)

#     return r.recognize_google(audio)


import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

