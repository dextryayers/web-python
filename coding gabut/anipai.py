import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Starting and Intializing AniipAI...")

MASTER = "haniip"

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evning" + MASTER)
        speak("")
        
#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google_cloud(audio, language="en-us")
        print(f"hanip said: {query}\n")
        
    except Exception as e:
        print("Ngomong sing gena oyyy....")
        query = None
        
    return query
    
#program start
speak("Hello my name is Jarwo bin sopo, can i help MR hanip?")
wishMe()
query = takeCommand()

#program perancangan
if "wikipedia" in (query or "").lower():
    speak("jek golek nek wikipedia harap sabar...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)


        