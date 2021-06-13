import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjoke



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

def wishme():
    speak("namaskaar")

    hour=datetime.datetime.now().hour

    if hour>=6 and hour<= 12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour >=18 and hour <+24:
        speak("good evening")
    else:
        speak("good night")

    speak("How can I help you?")
    
    
#wishme()

   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,'en=IN')
        print(query)
    except Exception as e:
        print(e)
        speak("I can't understand...please repeat again")
        return"None"
    return query

#takeCommand()

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("text@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Lenovo\\Desktop\\Guruji\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)


    battery = psutil.sensors_batttery
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjoke.get_jokes())



# Driver


    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif"offline" in query :
            quit()
        elif "wikipedia" in query :
            speak("Searching...")
            query = query .replace("wikipedia","")
            result = wikipedia.summary(query,sentences =2)
            speak(result)
        elif "send email" in query :
            try:
                speak("What should I say?")
                content =takeCommand()
                to ="xyz@gmail.com"
                #sendmail(to, content)
                speak(content)

            except Exception as e:
                speak(e)
                speak("Unable to send the meassage")

        elif "search in chrome" in query :
            speak("What should I search ?")
            chromepath="C:\Program Files (x86)\Google.exe %s"
            search =takeCommand().lower()
            wb.get(chromepath).oprn_new_tab(search + ".com")
        
        elif "logout" in query :
            os.system("shutdown -1")

        elif "shutdown" in query :
            os.system("shutdown /s /t 1")
        
        elif "restart" in query :
            os.system("shutdown /r /t 1")
        
        elif"play songs" in query:
            songs_dir ="F:\musics\music"
            songs =os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        
        elif"remember that" in query :
            speak("what should I remember?")
            data =takeCommand()
            speak("You said to remember"+ data)
            remember =open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open ("data.txt","r")
            speak("You said me to remember that"+remember.read())

        elif "screenshot" in query :
            screenshot()
            speak("Done")

        elif "cpu" in query :
            cpu()

        elif "joke" in query :
            jokes()