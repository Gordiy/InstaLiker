import telebot
import sys
import time
from constants import token
from InstagramAPI import InstagramAPI
# from set import SetLike
from set_like2 import SetLike



bot = telebot.TeleBot(token)

login = ""

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True)
    user_murkup.row('/start')
    user_murkup.row('Yes', 'No')
    user_murkup.row('Private', 'No private')
    msg = bot.send_message(message.from_user.id, "Hello☺☺☺ Do you want to increase likes to your instagram???",
                     reply_markup=user_murkup)
    bot.send_message(message.from_user.id, "Привіт ☺☺☺ Ти хочеш збільшити кількість лайків в твоєму Intstagram профілі?")
    # msg = bot.reply_to(message, "Hello, do you want to increase likes to your instagram?")
    bot.register_next_step_handler(msg, process_private_step)


def process_private_step(message):
    if message.text == 'Yes':
        bot.send_message(message.from_user.id, "You must to subscribe on https://t.me/sportnews445")
        bot.send_message(message.from_user.id, "Ти повинен підписатися на https://t.me/sportnews445")
        time.sleep(8)
        msg = bot.reply_to(message, "Your profile should not be private.")
        bot.send_message(message.from_user.id, "Бажано, щоб твій профіль не був приватним.")
        bot.register_next_step_handler(msg, login_and_pswd_step)
    if message.text == 'No':
        bot.send_message(message.from_user.id, "Good luck")


def login_and_pswd_step(message):
    if message.text == 'Private' or message.text == 'Yes':
        bot.send_message(message.from_user.id, "Sorry, you profile must be not private. 😰")
        bot.send_message(message.from_user.id, "Вибач, але твій профіль є приватним, щоб спробувати знову нажми /start")
    elif message.text == 'No private' or message.text == 'No':
        msg = bot.send_message(message.from_user.id, "Bot need your login and password that to increase likes. All data are private.")
        bot.send_message(message.from_user.id, "Боту необхідний тві логін і пароль, щоб збільшити кількість лайків в твоєму Instagram. Всі дані є шифрованими і не можуть бути використані ніде окрім цього бота.")
        bot.send_message(message.from_user.id, "Enter login / Введи логін будь ласка : ")
        bot.register_next_step_handler(msg, login_step)


def login_step(message):
    if (message.text):
        global login
        login = message.text
        # bot.send_message(message.from_user.id, login)
        msg = bot.send_message(message.from_user.id, "Enter password to your instagram profile / Введи пароль до твого Instagram : ")
        bot.register_next_step_handler(msg, pswd_step)


def pswd_step(message):
    if message.text:
        pswd = message.text
        # bot.send_message(message.from_user.id, login)

        log = InstagramAPI(str(login), pswd)

        if log.login():
            bot.send_message(message.from_user.id, "You will obtain likes for 12 hour ☺️☺️☺️")
            bot.send_message(message.from_user.id, "Ти отримаєш лайки приблизно через 12 годин ☺️☺️☺")

            set_like = SetLike(login=login, password=pswd)
            set_like.liking()

            bot.send_message(message.from_user.id, "You obtain your like )))")
        else:
            bot.send_message(message.from_user.id, "Your login or password is incorrect. If you want try again press /start button.")
            bot.send_message(message.from_user.id, "Неправильний логін або пароль. Якщо хочеш спробувати знову натисни кнопку /start")

        # msg = bot.send_message(message.from_user.id, "Pleace wait 1 minute, we must chech if your credentials are correct.")

# bot.polling(True)

while True:

    try:

        bot.polling(none_stop=True)

    # ConnectionError and ReadTimeout because of possible timout of the requests library

    # TypeError for moviepy errors

    # maybe there are others, therefore Exception

    except Exception as e:


        time.sleep(15)