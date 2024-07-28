from telebot import *
import re
import random

api = '6883012534:AAE9KG9KhgLbqEAXbERxSlc7q2MOrkJLA4Q'
bot = TeleBot(api) 

# start
@bot.message_handler(commads=['start'])
def selamat_datang(message):
    bot.reply_to(message, 'Halooo Aniipp')
    
bot.infinty_polling(True)