import psutil
import os
import telebot
from dotenv import load_dotenv

load_dotenv(override=True)

battery = psutil.sensors_battery()
percent = int(battery.percent)
status = battery.power_plugged
pc_name = os.getenv('PC_NAME')

message = f"{pc_name} battery percent is {percent}%"
print(message)

if percent <= 20 and status is False:
    bot_key = os.getenv('BOT_KEY')
    chat_id = os.getenv('CHAT_ID')

    bot = telebot.TeleBot(bot_key)
    bot.send_message(chat_id, message)
