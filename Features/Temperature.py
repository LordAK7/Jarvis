from bs4 import BeautifulSoup
import requests
import pyttsx3
import speech_recognition as sr

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

def Temp():
    search = "temperature in mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    Speak(f"The Temperature Outside Is {temperature}")

    Speak("Do I Have To Tell You Another Place Temperature ?")
    next = TakeCommand()

    if 'no' in next:
        Speak("Okay sir no problem")

    else:
        Speak("Tell Me The Name Of tHE Place ")
        name = TakeCommand()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature is {temperature} ")