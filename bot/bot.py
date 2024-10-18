import telebot
from dotenv import load_dotenv
import os
from links import links_info

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    msg = """Welcome to butterflyai dapp analyser bot!
    
    """
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['scan'])
def send_scan_prompt(message):
    bot.reply_to(message, "Please send a link to scan.")


@bot.message_handler(func=lambda message: True)
def handle_link(message):
    link_ = str(message.text.strip())
    link = link_.lower()
    domain = link.split('//')[-1].split('/')[0] 
    
    if domain in links_info:
        bot.send_message(message.chat.id, links_info[domain])
    else:
        bot.send_message(message.chat.id, "The link is not recognized.")

# Start the bot
bot.polling()