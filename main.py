import pyttsx3
import speech_recognition as sr
import webbrowser
from Features import  Temperature 
import os 
import random

def Speak(audio):
    engine = pyttsx3.init('sapi5') #sapi5 for windows , espeak for linux -i dont linke the sound of espeak so using sapi 5 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id) #sapi 5 voice id
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source: #device index for multiple microphones
        print(": Listening....")
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio)
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()

def TaskExe():
 
    while True:

        query = TakeCommand()

        if 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'temperature' in query:
            Temperature.Temp()

        elif 'play music' in query:
            music_folder = "C:\\Users\\vijay\\OneDrive\\Desktop\\Jarvis-Git\\main.py\\Database\\"
            music = ['hokage', 'oski', 'rocstar']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            Speak('Okay, here is your music! Enjoy!')
                  
        else:
            print("none")



TaskExe()