from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# kv = Builder.load_file("Ex31Screens.kv")

# Screens


class MainWindow(Screen):
    pass


class RequestSatisfaction(Screen):
    pass


class CertificateConverter(Screen):
    pass


class WindowsManager(ScreenManager):
    pass


class Ex31Screens(App):
    # def build(self):
    #     return kv  # For screenmanager
    pass


if __name__ == '__main__':
    Ex31Screens().run()
