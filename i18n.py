# core/i18n.py

import gettext
import os
import builtins

# --- 配置常量 ---
# 使用绝对路径来定位项目根目录，这样更健壮
# os.path.dirname(__file__) 是 'core' 目录
# os.path.dirname(...) 是项目根目录
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

APP_NAME = "messages"
LOCALE_DIR = os.path.join(_PROJECT_ROOT, "translations")


def get_user_language() -> str:
    """
    在这里实现获取用户语言的逻辑。
    这是一个示例，它会尝试从环境变量获取，如果失败则返回 'zh_CN'。
    """
    return "zh_CN"


def setup_translations(language_code: str = None):
    """
    查找并安装指定语言的翻译。

    如果在全局作用域（builtins）中安装了 _() 函数，
    这样项目中的任何文件都无需导入即可直接使用。
    """
    if language_code is None:
        language_code = get_user_language()

    try:
        # 寻找 .mo 文件并加载
        translation = gettext.translation(
            APP_NAME, 
            localedir=LOCALE_DIR, 
            languages=[language_code]
        )
        
        # 在全局安装 _() 函数
        translation.install()
        print(f"成功加载语言: {language_code}")
        
    except FileNotFoundError:
        print(f"警告：找不到语言 '{language_code}' 的翻译文件，将使用默认文本。")
        # 如果找不到，安装一个“什么都不做”的 _() 函数以避免程序崩溃
        builtins.__dict__['_'] = lambda text: text

