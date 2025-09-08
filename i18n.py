import gettext
import os

_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_NAME = "messages"
LOCALE_DIR = os.path.join(_PROJECT_ROOT, "translations")

def get_user_language() -> str:
    return "zh_CN"

def get_translator(language_code: str = None):
    if language_code is None:
        language_code = get_user_language()

    try:
        translation = gettext.translation(
            APP_NAME,
            localedir=LOCALE_DIR,
            languages=[language_code]
        )
        return translation.gettext  # 返回 gettext 函数
    except FileNotFoundError:
        print(f"警告：找不到语言 '{language_code}' 的翻译文件，将使用默认文本。")
        return lambda text: text  # 返回原样返回的函数