import requests
import wikipedia
import pywhatkit as kit
import smtplib
import webbrowser
import pyautogui
import time

from email.message import EmailMessage
from decouple import config

EMAIL = <Your Email>
PASSWORD = <Your PassKey>



def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def search_on_google(query):
    kit.search(query)


def youtube(video):
    kit.playonyt(video)

def send_email(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL

        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-27&sortBy=general&apiKey"
                          f"=<Your API Key>").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

def weather_forecast(city):
        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<Your API Key>"
    ).json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

def open_amazon():
    try:
        # Open Google first
        webbrowser.open('https://www.google.com')
        time.sleep(2)  # Wait for Google to load
        
        # Type "amazon" and press enter
        pyautogui.write('amazon')
        pyautogui.press('enter')
        time.sleep(2)  # Wait for search results
        
        # Click on the first result (usually Amazon's main site)
        pyautogui.click(x=200, y=300)  # Adjust these coordinates based on your screen
        return True
    except Exception as e:
        print(f"Error opening Amazon: {e}")
        return False
