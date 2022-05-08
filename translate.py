
"""This programme is translator for Telegram bot"""


from googletrans import Translator

trans = Translator()


def ua_to_en(words):
    """This function translates input text
    from ukrainian to english language"""
    translation = trans.translate(words, src='uk', dest='en')
    return translation.text

def ua_to_de(words):
    translation = trans.translate(words, src='uk', dest='de')
    return translation.text

languages = ['English', 'German']

# print(ua_to_en("що робиш"))