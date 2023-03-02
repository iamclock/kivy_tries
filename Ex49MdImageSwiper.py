"""
Image Swiper example exercise 49
"""

import os
from kaki.app import App
from kivy.factory import Factory
# from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


# почему то абсолютный путь при запуске становится на уровень выше, из-за этого приходится прописывать явно
module_root_dir = os.path.abspath("w:/MyProjects/Python/kivy_tries")


class SomeScreen(MDScreen):
    # Builder.load_file("Ex49MdImageSwiper.kv")  # вызов метода оказывает эффект раздвоения изображения
    # => класс и название файла с разметкой должны называться по-разному, либо убрать явный вызов метода класса builder
    pass


class Ex49MdImgSwiper(App, MDApp):

    dialog = None
    CLASSES = dict(SomeScreen="Ex49MdImageSwiper")
    AUTORELOADER_PATHS = ((".", dict(recursive=True)),)
    # с совпадающим названием класса с файлом .kv происходит двойная загрузка файла .kv из-за чего начинаются происходят глюки
    KV_FILES = (os.path.join(module_root_dir, "Ex49MdImageSwiper.kv"),)
    # KV_FILES = ("Ex49MdImageSwiper.kv",)

    def build_app(self, *args):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        print("DEBUG =", os.getenv("DEBUG"))
        return Factory.SomeScreen()


if __name__ == "__main__":
    Ex49MdImgSwiper().run()


'''
class Ex49MdImageSwiper(MDApp):

    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return
        # return Builder.load_file("Ex49MdImageSwiper.kv")


if __name__ == "__main__":
    Ex49MdImageSwiper().run()
'''
