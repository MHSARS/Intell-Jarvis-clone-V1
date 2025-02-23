import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
import imdb
import wolframalpha
import pyautogui
import webbrowser

from decouple import config
from datetime import datetime
from random import choice

from conv import random_text
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email, get_news, weather_forecast, open_amazon

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 215)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you?")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en')
        print(query)

        if not 'stop' in query or 'exit' in query:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir")
            else:
                speak("Have a good day sir")
            exit()
    except Exception:
        speak("Sorry I couldn't understand that, can you please repeat that?")
        query = 'None'
    return query


if __name__ == '__main__':
    greet_me()

    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am good sir, what about you.")
            elif "open command prompt" in query:
                speak("Opening command prompt sir")
                os.system('start cmd')
            elif "open visual studio" in query:
                visualstudio_path = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(visualstudio_path)
            elif "open webstorm" in query:
                webstorm_path = "C:\\Program Files\\JetBrains\\WebStorm 2024.3.1\\bin\\webstorm64.exe"
                os.startfile(webstorm_path)
            elif "open notepad" in query:
                speak("Opening notepad sir")
                notepad_path = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(notepad_path)
            elif "open discord" in query:
                speak("Opening Discord for you sir")
                discord_path = "C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
                os.startfile(discord_path)
            elif "ip address" in query:
                ip_address = find_my_ip()
                speak(
                    f"Your ip address is {ip_address}"
                )
                print(f"ip address: {ip_address}")
            elif "open youtube" in query:
                speak("What would you like to play on youtube sir?")
                video = take_command().lower()
                youtube(video)
            elif "open google" in query:
                speak("what would you like to search on google sir?")
                query = take_command().lower()
                search_on_google(query)
            elif "wikipedia" in query:
                speak("what would you like to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia, {results}")
                speak("I am printing reaults on the terminal")
                print(results)
            elif "send an email" in query:
                speak("who's email would you like to send it to. Enter in the terminal")
                receiver_add = input ("Email Address: ")
                speak("what is the subject sir")
                subject = take_command().capitalize()
                speak("what is the message")
                message = take_command().capitalize()
                if send_email(receiver_add, subject, message):
                    speak("Email sent successfully sir")
                    print("Email sent successfully sir")
                else:
                    speak("Something went wrong, please check the error log")
            elif "give me news" in query:
                speak(f"Here are the latest headlines for today sir")
                speak(get_news())
                speak("I am also printing it on the screen sir")
                print(*get_news(), sep='\n')
            elif "weather" in query:
                ip_address = find_my_ip()
                speak("tell me the name of your city in the terminal")
                city = input("Enter name of your city: ")
                speak(f"Getting weather report of your location {city}")
                weather, temp, feels_like = weather_forecast(city)
                speak(f"The current tempreture is {temp}, but feels like {feels_like}")
                speak(f"Also the weather report talks about {weather}")
                speak("I am printing the weather information on the screen sir")
                print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
            elif "movie" in query:
                movies_db = imdb.IMDb()
                speak("Please tell me the movie name sir:")
                text = take_command()
                movies = movies_db.search_movie(text)
                speak("Searching for: " + text)
                speak("I found these")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}-{year}")
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info["cast"]
                    actor = cast[0:5]
                    plot = movie_info.get('plot outline', 'plot summary not available')
                    speak(f"{title} was released in {year} has imdb rating of {rating}. Its cast includes: {actor}. The plot summary of the movie is {plot}")
                    print(f"{title} was released in {year} has imdb rating of {rating}. Its cast includes: {actor}. The plot summary of the movie is {plot}")
            elif "calculate" in query:
                app_id = "RRKRAY-HUYHU42Q48"
                client = wolframalpha.Client(app_id)
                ind = query.lower().split().index("calculate")
                text = query.split()[ind + 1:]
                result = client.query(" ".join(text))
                try:
                    ans = next(result.results).text
                    speak("The answer is" + ans)
                    print("The answer is" + ans)
                except StopIteration:
                    speak("I couldn't find that. Please try again")
            elif "what is" in query or "who is" in query or "which is" in query:
                app_id = "RRKRAY-HUYHU42Q48"
                client = wolframalpha.Client(app_id)
                try:
                    ind = query.lower().index('what is') if 'what is' in query.lower() else \
                        query.lower().index('who is') if 'who is' in query.lower() else \
                        query.lower().index('which is') if 'which is' in query.lower() else None

                    if ind is not None:
                        text = query.split()[ind + 2:]
                        result = client.query(" ".join(text))
                        ans = next(result.results).text
                        speak("The answer is: " + ans)
                        print("The answer is: " + ans)
                    else:
                        speak("I could not find the answer to that")
                except StopIteration:
                    speak("I couldn't find that. Please try again sir")
            elif "amazon" in query:
                speak("Opening Amazon for you sir")
                if open_amazon():
                    speak("Successfully opened Amazon")
                else:
                    speak("I encountered an error while trying to open Amazon")