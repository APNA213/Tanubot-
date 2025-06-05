import telebot  
import os  
import random  
from keep_alive import keep_alive  
import requests  
  
TOKEN = os.getenv("8007225178:AAF9vyVzC9HM96jTFs5QXsGcDy0dtte0q38")  
OWNER_ID = 7390472005  
bot = telebot.TeleBot("8007225178:AAF9vyVzC9HM96jTFs5QXsGcDy0dtte0q38")  
  
def get_weather():  
    return "Aaj ka mausam: romantic aur thoda thoda pyaar bhara ❤️☁️"  
  
def chat_with_ai(message):  
    return f"Tumne bola: {message} — aur mujhe toh har baat pyaari lagti hai 😊"  
  
def romantic_reply(msg):  
    return f"{msg} 💖 Tum ho toh sab kuch hai..."  
  
jokes = [  
    "Tumhare bina toh mausam bhi udaas lagta hai 💕",  
    "Tum hanso toh lagta hai duniya jeet li 😄",  
    "Ek joke: Tum aur main – perfect combo 😘"  
]  
  
gif_urls = [  
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",  
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"  
]  
  
@bot.message_handler(func=lambda message: True, content_types=['text'])  
def handle_all(message):  
    text = message.text.lower()  
    uid = message.from_user.id  
    uname = message.from_user.username or "unknown"  
  
    if "weather" in text or "mausam" in text:  
        bot.reply_to(message, get_weather())  
  
    elif "joke" in text:  
        bot.reply_to(message, romantic_reply(random.choice(jokes)))  
  
    elif "gif" in text:  
        bot.send_animation(message.chat.id, random.choice(gif_urls))  
  
    else:  
        response = chat_with_ai(message.text)  
        if uid == OWNER_ID:  
            bot.reply_to(message, romantic_reply(response))  
        else:  
            bot.reply_to(message, response)  
  
@bot.message_handler(content_types=['new_chat_members'])  
def welcome_new_member(message):  
    for member in message.new_chat_members:  
        name = member.first_name  
        bot.send_message(  
            message.chat.id,  
            f"Hey {name} 👋 Welcome to the group! Tanu yahan hai dosti aur hasi ke liye 😄"  
        )  
  
keep_alive()  
print("Tanu is online in group and private – sweet, smart & romantic 💋")  
bot.infinity_polling()