# Dial button menu example exercise 47
from kivy.lang import Builder
from kivymd.app import MDApp

# https://kivymd.readthedocs.io/en/1.1.1/components/button/index.html#mdfloatingactionbuttonspeeddial


class Ex47MdDialButtonMenu(MDApp):

    class Orientation(object):
        vertical = "vertical"
        horizontal = "horizontal"

    presets: tuple = ("Hello <username>",
                      "Already logged in", "Well again",
                      "Over and over and over again", "...")
    preset_ind: int = 0
    data: dict = dict((("Python", "language-python"),
                       ("Ruby", "language-ruby"),
                       ("Java", "language-java")))

    preset_length: int = len(presets)

    def callback(self, instance):
        self.root.ids.my_label.text = f"{instance.icon}"
        return

    def open(self):
        self.root.ids.my_label.text = f"opened"
        return

    def close(self):
        self.root.ids.my_label.text = f"closed"
        return

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex47MdDialButtonMenu.kv")


if __name__ == "__main__":
    Ex47MdDialButtonMenu().run()
