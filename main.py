import pyttsx3
import speech_recognition as sr
import webbrowser

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
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

        else:
            print("none")



TaskExe()