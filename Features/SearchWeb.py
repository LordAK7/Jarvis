import webbrowser as web
import pywhatkit
import pyttsx3
import speech_recognition as sr

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

def Speak(audio):
    engine = pyttsx3.init('sapi5') #sapi5 for windows , espeak for linux -i dont linke the sound of espeak so using sapi 5 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id) #sapi 5 voice id
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")


def YoutubeSearch(Query):
    Query1 = Query.lower()
    Query1 = Query.replace("youtube search","")
    result = "https://www.youtube.com/results?search_query=" + Query1
    web.open(result)
    Speak("Enjoy your video sir!")
    pywhatkit.playonyt(Query)
    Speak("This may also be good for you")

def Image(Query):
    try:
        url = "https://photos.google.com/" + Query
        web.open(url)
    except Exception as e:
        print(e)
        return False