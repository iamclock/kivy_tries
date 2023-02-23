# Color themes example exercise 43
from kivymd.app import MDApp


class Ex43MdColorThemes(MDApp):

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        return


if __name__ == "__main__":
    Ex43MdColorThemes().run()