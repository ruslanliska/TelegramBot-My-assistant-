import logging

import pyowm
import telebot
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from telebot import types

from config import OWM_TOKEN, TOKEN
from news import BotArticles
from translate import ua_to_en, ua_to_de
from weather import get_forecast
from utils import Logger

bot = telebot.TeleBot(TOKEN)
owm = OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome_start(message):
    """Greets used after /start command."""
    send_mess = f"""<b>Привіт {message.from_user.first_name}!</b> \nЯ дуже радий тебе бачити
                    \nЯк у тебе справи?"""
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['menu'])
def default_menu(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_weather = types.InlineKeyboardButton(text='Погода',
                                              callback_data='weather')
    item_news = types.InlineKeyboardButton(text='Новини',
                                           callback_data='news')
    item_quiz = types.InlineKeyboardButton(text="Перекладач",
                                           callback_data="translate")
    markup_inline.add(item_news, item_weather, item_quiz)
    bot.send_message(message.chat.id, "Будь ласка, вибери необхідний пункт",
                     reply_markup=markup_inline)


@bot.message_handler(commands=['help'])
def send_message_help(message):
    """Reply to /help command with message."""
    bot.send_message(message.chat.id, "Я буду допомагати тобі всім чим зможу")


@bot.message_handler(content_types=['text'])
def ask_for_help(message):
    """Reply to all unknown text with menu buttoms."""
    if message.text.lower() == "добре":
        bot.send_message(message.chat.id, "Я радий, що в тебе все добре")
    default_menu(message)


@bot.callback_query_handler(func=lambda call: call.data == 'weather')
def command_weather(call):
    """
    Takes call "weather" and ask for city for detailed forecast
    and direct message to send_forecast function.
    """
    sent = bot.send_message(call.message.chat.id, "🗺 Будь ласка, вкажи місто у якому ти хочеш дізнатися погоду\n")
    bot.register_next_step_handler(sent, send_forecast)


def send_forecast(message):
    """Take city name and returns forecast."""
    try:
        forecast = get_forecast(message.text)
        bot.send_message(message.chat.id, forecast)
    except pyowm.commons.exceptions.NotFoundError as e:
        logging.error("No city found for user and error handled. User asked to enter city again")
        bot.send_message(message.chat.id,
                         """❌  Нажаль я не можу знайти таке місто! \nБудь ласка, перевірь ще раз та спробуй знову!""")
        default_menu(message)


@bot.callback_query_handler(func=lambda call: call.data == 'news')
def command_news(call):
    """Take call and ask for title in News and sends message to user."""
    bot.send_message(call.message.chat.id, "🆕 Ось найважливіші новини на даний момент:\n")
    for i in BotArticles.get_article():
        bot.send_message(call.message.chat.id, i, parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data == "translate")
def command_translate(call):
    """Take call translate and ask user for language which preffered to translate"""
    trans_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True)
    trans_markup.row('English', 'German')
    sent = bot.send_message(call.message.chat.id, "📃 Будь ласка, уточни мову на яку ти бажаєш перекласти",
                            reply_markup=trans_markup)
    bot.register_next_step_handler(sent, get_input)


languages = ['English', 'German']


def get_input(message):
    """Check whether language is avaliable and ask for text to be translated."""
    if not any(message.text in item for item in languages):
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "❌ Нажаль я незнаю такої мови. Будь ласка, обери з меню нижче",
                         reply_markup=hide_markup)
    else:
        sent = bot.send_message(message.chat.id,
                                f"🚩 Ти обрав таку мову: {message.text} \n➡️ Введи текст, який бажаєш перекласти")
        languages_switcher = {'English': send_eng_trans, 'German': send_de_trans}
        lang_response = languages_switcher.get(message.text)
        bot.register_next_step_handler(sent, lang_response)


def send_eng_trans(message):
    """Send message of translated ukrainian to english text."""
    bot.reply_to(message, ua_to_en(message.text))


def send_de_trans(message):
    bot.reply_to(message, ua_to_de(message.text))


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    Logger()
    main()
