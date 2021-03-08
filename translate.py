
"""This programme is translator for Telegram bot"""


from googletrans import Translator

trans = Translator()


def ua_to_en(words):
    """This function translates input text
    from ukrainian to english language"""
    translation = trans.translate(words, src='uk', dest='en')
    return translation.text


languages = ['English']

# print(ua_to_en("що робиш"))