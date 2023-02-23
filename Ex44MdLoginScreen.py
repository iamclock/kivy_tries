# Login screen example exercise 44
from kivymd.app import MDApp
from kivy.lang import Builder


class Ex44MdLoginScreen(MDApp):
    presets: tuple = ("Hello <username>",
                      "Already logged in", "Well again",
                      "Over and over and over again", "...")
    preset_ind: int = 0
    preset_length: int = len(presets)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex44MdLoginScreen.kv")

    def logger(self) -> None:
        self.root.ids.welcome_label.text = self.presets[self.preset_ind]
        self.preset_ind = (self.preset_ind + 1) % self.preset_length
        return

    def clear(self) -> None:
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
        return


if __name__ == "__main__":
    Ex44MdLoginScreen().run()
