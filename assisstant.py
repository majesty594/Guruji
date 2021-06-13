import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("Hi I am Guruji your virtual assistant")

def time():
    Time = datetime.datetime.now().strftime("%h:%M:%S")
    speak(Time)
#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date =int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)

#date()
