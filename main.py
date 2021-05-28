# import speech_recognition as sr

# listener = sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print("lishing...")
#         voice = listener.listen(source)
#         command = listener.recognize_google(voice)
#         print(command)
# except:
#     pass
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


