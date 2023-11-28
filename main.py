import psutil
import os
import telebot
from dotenv import load_dotenv

battery = psutil.sensors_battery()
percent = int(battery.percent)
status = battery.power_plugged

charging = "Charging" if status else "Not Charging"
message = f"Battery percent is {percent}% and it is {charging}"
print(message)

if percent <= 20 and status is False:
    load_dotenv()
    bot_key = os.getenv('BOT_KEY')
    chat_id = os.getenv('CHAT_ID')

    bot = telebot.TeleBot(bot_key)
    bot.send_message(chat_id, message)
