import psutil
import os
import telebot
from dotenv import load_dotenv


battery = psutil.sensors_battery()
percent = int(battery.percent)
status = battery.power_plugged

message = f"Battery percent is {percent}%"
print(message)

if percent <= 20 and status is False:
    load_dotenv(override=True)
    bot_key = os.getenv('BOT_KEY')
    chat_id = os.getenv('CHAT_ID')

    bot = telebot.TeleBot(bot_key)
    bot.send_message(chat_id, message)
