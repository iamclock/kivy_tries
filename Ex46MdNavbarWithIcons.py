# Navbar with icons example exercise 46
from kivy.lang import Builder
from kivymd.app import MDApp


class Ex46MdNavbarWithIcons(MDApp):
    presets: tuple = ("Hello <username>",
                      "Already logged in", "Well again",
                      "Over and over and over again", "...")
    preset_ind: int = 0
    preset_length: int = len(presets)

    class Orientation(object):
        vertical = "vertical"
        horizontal = "horizontal"

    class Halign(object):
        left = "left"
        center = "center"
        right = "right"

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex46MdNavbarWithIcons.kv")


if __name__ == "__main__":
    Ex46MdNavbarWithIcons().run()
