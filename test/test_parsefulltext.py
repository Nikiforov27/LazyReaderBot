from rhvoice_wrapper import TTS
import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent

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

parse_full_text("https://habr.com/ru/companies/otus/articles/560278/")
