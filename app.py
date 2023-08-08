from os import environ
import sys
from google.cloud import translate
import argparse

parser = argparse.ArgumentParser(description='A simple argument parser example.')
parser.add_argument('arg1', help='Text input')
parser.add_argument('-l', '--loud', action='store_true', help='Loud flag')
parser.add_argument('-ln', '--langs', help='List of supported languages', action='store_true')
parser.add_argument('-lang', '--chooselang', help='Translate to', action='store', default='en_US', required=False)

args = parser.parse_args()


PROJECT_ID = environ.get("PROJECT_ID", "")
assert PROJECT_ID
PARENT = f"projects/{PROJECT_ID}"


def print_supported_languages(display_language_code: str):
    """
    Retrieves and prints the list of supported languages for translation.

    Args:
        display_language_code (str): The language code of the display language.

    Returns:
        None
    """
    client = translate.TranslationServiceClient()

    response = client.get_supported_languages(
        parent=PARENT,
        display_language_code=display_language_code,
    )

    languages = response.languages
    print(f" Languages: {len(languages)} ".center(60, "-"))
    for language in languages:
        language_code = language.language_code
        display_name = language.display_name
        print(f"{language_code:10}{display_name}")


def translate_text(text: str, target_language_code: str) -> translate.Translation:
    """
    Translates the given text into the specified target language using the Google Translate API.

    Args:
        text (str): The text to be translated.
        target_language_code (str): The language code of the target language.

    Returns:
        translate.Translation: An object representing the translated text.
    """

    client = translate.TranslationServiceClient()
    response = client.translate_text(
        parent=PARENT,
        contents=[text],
        target_language_code=target_language_code,
    )

    return response.translations[0].translated_text


# With any argument, print the translation and sound translation.

if args.loud:
    import play
    text = translate_text(sys.argv[1], "en_US")
    play.play_sound(text)
elif not args.loud and args.langs is False:
    text = translate_text(args.arg1, args.chooselang)
    print(text)
elif args.langs is True:
    print_supported_languages('en')



