import time
from transliterate import to_cyrillic, to_latin
import telebot
import logging

# Tokenni kiriting
TOKEN = '7872412856:AAFPkrs76AfRtJ_BcWMZKvoMzDynPZ7Hoi4'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(commands=['help'])
def send_help(message):
    javob = "Assalomu alaykum, Sizni oylantirgan har qanday savollar bo'yicha ushbu adminga murojat qiling"
    javob += "\n @rafiqjonov_2006"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        logging.info(f"Yangi xabar: {message.text}")
        msg = message.text
        if msg.isascii():
            javob = to_cyrillic(msg)
        else:
            javob = to_latin(msg)

        # So'zlarni kichik qismlarga bo'lish va kutish qo'shish
        chunk_size = 500  # Har bir javob uchun maksimal uzunlik
        for i in range(0, len(javob), chunk_size):
            bot.reply_to(message, javob[i:i + chunk_size])
            time.sleep(1)  # Har bir xabar orasida 1 sekund kutish
    except Exception as e:
        logging.error(f"Xatolik yuz berdi: {e}")

# Botni doimiy ishlashga sozlash
bot.infinity_polling(timeout=10, long_polling_timeout=5, skip_pending=True, thread=True)
