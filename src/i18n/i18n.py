import json
import locale
import os
from pathlib import Path

def load_language_list(language):
    # json_path = os.path.join(Path(__file__).resolve().parent, f"locale/ja_JP.json")
    # json_path = os.path.join(Path(__file__).resolve().parent, f"locale/en_US.json")
    # json_path = os.path.join(Path(__file__).resolve().parent, f"locale/zh_CN.json")
    # json_path = os.path.join(Path(__file__).resolve().parent, f"locale/zh_TW.json")    
    json_path = os.path.join(Path(__file__).resolve().parent, f"locale/{language}.json")
    with open(json_path, "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = locale.getdefaultlocale()[
                0
            ]  # getlocale can't identify the system's language ((None, None))
            
        json_path = os.path.join(Path(__file__).resolve().parent, f"locale/{language}.json")            
        if not os.path.exists(json_path):
            language = "en_US"
        self.language = language
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
