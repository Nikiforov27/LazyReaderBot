from rhvoice_wrapper import TTS
import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import telebot

bot = telebot.TeleBot("6863214237:AAEsROBNzBzXkxll20K2-QPye_SqEtKCRBA", parse_mode=None) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот который прочитает за тебя любую статью")
    bot.send_message(message.chat.id, "Просто скинь мне ссылку, а я вышлю тебе аудио файл")
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    ua = UserAgent()

    headers = {"User-Agent": ua.random}

    tts = TTS(threads=2)


    url = message.text
    #url = 'https://habr.com/ru/articles/779450/'

    full_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(full_page.content, 'lxml')

    convert = soup.find_all("p")

    words = []

    i = 0
    while i < len(convert):
        words.append(convert[i].text)
        i = i + 1

    audio_file_name = str(url[29] + url[30] + url[31] + url[32] + url[33] + url[34]) + '.mp3'

    tts.to_file(filename=audio_file_name, text=words, voice='anna', format_='opus', sets=None)

    audio = open(audio_file_name, 'rb')
    bot.send_audio(message.chat.id, audio)

bot.infinity_polling()
