# main.py
# -*- coding: utf-8 -*-
from i18n import setup_translations
setup_translations("zh_CN")
import customtkinter as ctk
from ui import NovelGeneratorGUI
def main():
    
    app = ctk.CTk()
    gui = NovelGeneratorGUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()
