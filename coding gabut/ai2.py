import speech_recognition as sr
import pyttsx3
import requests
import webbrowser
from youtube_dl import YoutubeDL
from pytube import YouTube
import random
#from googletrans import translator
import requests

# Inisialisasi speech recognition dan text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set suara wanita
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Suara wanita

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again please...")
            return "None"

def search_web(query):
    speak("Searching the web")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def get_news():
    speak("Getting the latest news")
    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=92b31789a7354e95b84f1615365a6673"
    response = requests.get(url)
    news = response.json().get("articles")
    for article in news[:5]:
        speak(article["title"])
        print(article["title"])

def play_music(video_url):
    speak("Playing music from YouTube")
    ydl_opts = {'format': 'bestaudio/best'}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        url = info_dict.get("url", None)
        webbrowser.open(url)
        
def play_youtube_video(query):
    speak("Opening YouTube")
    yt = YouTube(f"https://www.youtube.com/results?search_query={query}")
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    webbrowser.open(video.url)
    
def translate_text(text, dest_language):
    speak("Translating text")
    translation = translator.translate(text, dest=dest_language)
    translated_text = translation.text
    speak(f"The translation is: {translated_text}")
    print(f"Translated Text: {translated_text}")


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
        "you so handsome bro!"
    ]
    joke = random.choice(jokes)
    speak(joke)
    print(joke)
    
def support():
    quote = [
        "You are very handsome sirr"
        "You are very clever"
        "you're very good"
        
    ]
    support = random.choice(quote)
    speak(quote)
    print(quote)

# Main loop
if __name__ == "__main__":
    speak("Hello aassalamuualaaikummm hanipp, my name is oyenn how can I help you today MR hanip?")
    while True:
        query = listen().lower()

        if 'search' in query:
            search_web(query.replace("search", "").strip())
        elif 'news' in query:
            get_news()
        elif 'play music' in query:
            video_url = query.replace("play music", "").strip()
            play_music(video_url)
        elif 'open video' in query:
            video_query = query.replace("open video", "").strip()
            play_youtube_video(video_query)
        elif 'open browser' in query:
            file_manager()
        elif 'good morning' in query:
            speak('Good morning too sirr')
        elif 'good afternoon' in query:
            speak('Good afternoon too sirr')
        elif 'good night' in query:
            speak('Good night too sirr')
        elif 'joke' in query:
            tell_joke()
        elif 'support' in query:
            support()
        elif 'assalamualaikum' in query:
            speak("Waalaikumsalam haniipp can i help you sirr")
        elif 'thank you' in query:
            speak('youre welcome sir')
        elif 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break
        else:
            speak("I am sorry, I did not understand that.")
