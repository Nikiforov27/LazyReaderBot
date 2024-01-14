from rhvoice_wrapper import TTS
import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent


def parse_name_for_file(url):
    
    user_agent = UserAgent()
    headers = {"User-Agent": user_agent.random}

    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'lxml')
    convert = soup.find_all("h1")

    words_of_name = []

    i = 0
    while i < len(convert):
        words_of_name.append(convert[i].text)
        i = i + 1
    
    global audio_file_name
    audio_file_name = words_of_name[0] + ".mp3"
    
    print(audio_file_name)
    return audio_file_name

def parse_full_text(url):
        
    user_agent = UserAgent()
    headers = {"User-Agent": user_agent.random}

    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'lxml')
    convert = soup.find_all("p")

    words_of_full_text = []

    i = 0
    while i < len(convert):
        words_of_full_text.append(convert[i].text)
        i = i + 1

    global full_text
    full_text = ""

    n = 0
    while n < len(words_of_full_text):
        full_text = full_text + words_of_full_text[n]
        n = n + 1

    print(full_text)
    return full_text

def audio_maker(full_text):

    tts = TTS(threads=2)
    tts.to_file(filename=audio_file_name, text=full_text, voice='anna', format_='mp3', sets=None)
    return audio_file_name + "making succesfuly"

#parse_name_for_file("https://habr.com/ru/articles/761712/")
#parse_full_text("https://habr.com/ru/articles/761712/")
#audio_maker(parse_full_text("https://habr.com/ru/articles/761712/"))
