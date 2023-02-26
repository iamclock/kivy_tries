# Bottom bar button example exercise 45
from kivy.lang import Builder
from kivymd.app import MDApp


class Ex45MdBottomBarButton(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file("Ex45MdBottomBarButton.kv")

    def str_changing_on_pressing(self, msg):
        self.root.ids.my_label.text = msg
        return


if __name__ == "__main__":
    Ex45MdBottomBarButton().run()
