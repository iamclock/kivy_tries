# Dial button menu example exercise 47
from kivy.lang import Builder
from kivymd.app import MDApp

# https://kivymd.readthedocs.io/en/1.1.1/components/button/index.html#mdfloatingactionbuttonspeeddial


class Ex47MdDialButtonMenu(MDApp):

    data: dict = dict((("Python", "language-python"),
                       ("Ruby", "language-ruby"),
                       ("Java", "language-java")))

    def callback(self, instance):
        self.root.ids.my_label.text = f"{instance.icon}"
        return

    def open(self):
        self.root.ids.my_label.text = "opened"
        return

    def close(self):
        self.root.ids.my_label.text = "closed"
        return

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex47MdDialButtonMenu.kv")


if __name__ == "__main__":
    Ex47MdDialButtonMenu().run()
