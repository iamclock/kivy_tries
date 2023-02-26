# Navbar with icons example exercise 46
from kivy.lang import Builder
from kivymd.app import MDApp


class Ex46MdNavbarWithIcons(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex46MdNavbarWithIcons.kv")


if __name__ == "__main__":
    Ex46MdNavbarWithIcons().run()
