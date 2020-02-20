from core.error_handler import *
from core.functions import *

def translate(code):
    """
    Compile The Code That Passed As An Array.
    """

    # Open Repos ( Get Keywords From Repo Files)
    repos_handler = open("repos/html.txt")
    keywords = [i.replace("\n","") for i in repos_handler.readlines()]
    repos_handler.close()

    # Level 1 Translations
    search_array = ["@@" + i for i in keywords]
    replace_array = ["</" + i + ">" for i in keywords]
    translated_code = text_replacer(code,search_array,replace_array)

    # Level 2 Translations
    search_array = ["@" + i for i in keywords]
    replace_array = ["<" + i + ">" for i in keywords]
    translated_code = text_replacer(translated_code,search_array,replace_array)

    return translated_code
