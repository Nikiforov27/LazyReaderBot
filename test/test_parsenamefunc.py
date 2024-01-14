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
        
    print(words_of_name[0])
    return words_of_name[0]

parse_name_for_file("https://habr.com/ru/companies/otus/articles/560278/")
