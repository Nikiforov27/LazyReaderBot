import telebot

import audio_maker2

bot = telebot.TeleBot("6863214237:AAEsROBNzBzXkxll20K2-QPye_SqEtKCRBA", parse_mode=None) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот который прочитает за тебя любую статью на хабре")
    bot.send_message(message.chat.id, "Просто скинь мне ссылку, а я вышлю тебе аудио файл")
    

@bot.message_handler(func=lambda message: True)
def send_audio_message(message):
    audio_maker(parse_full_name(message.text))
    
    audio = open(parse_name_for_file(message.text), 'rb')
    bot.send_audio(message.chat.id, audio)

bot.infinity_polling()
