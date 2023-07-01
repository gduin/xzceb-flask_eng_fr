"""Importing MyMemoryTranslator from deep_translator"""
from deep_translator import MyMemoryTranslator as myMT

#Defining constants

CONST_ENGLISH='en-US'
CONST_FRENCH='fr-FR'


def translate_text(source_lang, target_lan, text):
    """translate_text function wrapping a library translator"""
    return myMT(source=source_lang, target=target_lan).translate(text)





def translate_english_to_french(english_text):
    """translate_english_to_french translate an english text to french language"""
    return translate_text(CONST_ENGLISH, CONST_FRENCH, english_text)






def translate_french_to_english(french_text):
    """translate_french_to_english translate an french text to english language"""
    return translate_text(CONST_FRENCH, CONST_ENGLISH, french_text)
