from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('LA1dZ74ZDtwu3OscISK0XkiW_O-W6_T0txR_I9N7m19i')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/c29ad1c2-2c46-4a81-a246-3b4eac320a4e')


def english_to_french(english_text):
    '''translation from english to french'''
    if english_text is None:
        return "Please provide valid English text to translate."

    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''translation from french to english'''
    if french_text is None:
        return "Please provide valid French text to translate."
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text["translations"][0]["translation"]

english_text = "Hello"
french_text = english_to_french(english_text)
print(f'Translation of "{english_text}" is "{french_text}"')

french_text = "Bonjour"
english_text = french_to_english(french_text)
print(f'Translation of "{french_text}" is "{english_text}"')